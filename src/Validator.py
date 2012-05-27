
# * is not under control of the network manager
# * has IPv6 disabled
# * has no IPv4/IPv6 addresses assigned to the interface
# * has locally generated egress L3 traffic blocked with iptables

import re
import subprocess
from src.Outcome import PositiveOutcome, NegativeOutcome


def iface_in_ifstates(iface):
    ''' This function returns True if given interface is present in the ifstate file. '''
    for ifstate_line in open('/var/run/network/ifstate'):
        ifstate_iface = ifstate_line.split('=')[0]
        if iface == ifstate_iface:
            return True
    return False


def iface_status(iface):
    status = dict()
    output = subprocess.check_output(['ethtool', iface])
    for line in output.split('\n'):
    	m = re.search('^\s+([^:]+?):\s+(\S+)\s*$', line)
    	if m:
		if m.group(1) == 'Speed':
			status['speed'] = m.group(2)
		elif m.group(1) == 'Duplex':
			status['duplex'] = m.group(2)
		elif m.group(1) == 'Link detected':
			status['link_detected'] = m.group(2)
    return status


def iface_has_ipv6_enabled(iface):
    ''' This function returns True if given interface has IPv6 enabled. '''
    sysctl_varname = 'net.ipv6.conf.%s.disable_ipv6' % iface
    sysctl_varvalue = subprocess.check_output(['sysctl', '-n', sysctl_varname])
    return (sysctl_varvalue.rstrip() != '1')


def iface_l3_addresses(iface):
    ''' This function returns a list of L3 addresses associated with given interface '''
    ip_addr_list = subprocess.check_output(['ip', 'addr', 'list', 'dev', iface])
    ip_addr_list_lines = ip_addr_list.split('\n')

    # check the first line of the output is as expected
    if len(ip_addr_list_lines) < 1:
        raise RuntimeError('iproute2 has reported no addresses for iface %s' % iface)
        # 3: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP qlen 1000
    line0_match = re.search('^\d+: (\w+):', ip_addr_list_lines[0])
    if line0_match is None or line0_match.group(1) != iface:
        raise RuntimeError('cannot first line of iproute2 "ip addr list": %s' % ip_addr_list_lines[0])

    # check the remaining lines of the output contain nothing besides Layer-2 addresses
    l3_addresses = []
    for ip_addr_list_line in ip_addr_list_lines[1:]:
        # link/ether 00:27:10:ea:51:f4 brd ff:ff:ff:ff:ff:ff
        # inet 10.252.48.103/24 brd 10.252.48.255 scope global wlan0
        if len(ip_addr_list_line) == 0: continue
        line_match = re.search('^\s+(\w+)', ip_addr_list_line)
        if line_match is None or line_match.group(1) != 'link':
            l3_addresses.append(ip_addr_list_line)

    if len(l3_addresses) == 0:
        return None
    else:
        l3_addresses.insert(0, ip_addr_list_lines[0])
        return l3_addresses


class IfaceMitmSuitabilityCheck(object):
    def __init__(self, iface):
        self.iface = iface
        self.res = dict()

    def run(self):
        self.check_nm()
        self.check_ipv6()
        self.check_l3_addrs()

    def check_nm(self):
        self.is_under_nm = iface_in_ifstates(self.iface)
        if self.is_under_nm:
            self.res['os_network_manager'] = NegativeOutcome(
                'The interface is under control of network-manager. This might create unwanted interference.',
                "To take the interface from under control of network-manager run 'sudo ifdown %s'." % self.iface
            )
        else:
            self.res['os_network_manager'] = PositiveOutcome('The interface is not under control of network-manager.')

    def check_ipv6(self):
        self.ipv6_enabled = iface_has_ipv6_enabled(self.iface)
        if self.ipv6_enabled:
            self.res['ipv6_addrs'] = NegativeOutcome(
                'The interface has IPv6 addresses configured.',
                "To disable IPv6 on this interface run 'sudo sysctl -w net.ipv6.conf.%s.disable_ipv6=1'." % self.iface
            )
        else:
            self.res['ipv6_addrs'] = PositiveOutcome('No IPv6 addresses assigned to the interface.')

    def check_l3_addrs(self):
        l3_addrs = iface_l3_addresses(self.iface)
        if l3_addrs:
            if self.is_under_nm and self.ipv6_enabled:
                solution = 'Taking the interface from under control of network-manager and disabling IPv6 might resolve the problem.'
            elif self.is_under_nm:
                solution = 'Taking the interface from under control of network-manager might resolve the problem.'
            elif self.ipv6_enabled:
                solution = 'Disabling IPv6 on the interface might resolve the problem.'
            else:
                solution = "The addresses appear to be assigned manually. Make sure there are "\
                           "no active DHCP clients, then de-configure the addresses with 'ifconfig'."
            self.res['l3_addrs'] = NegativeOutcome(
                'The interface has Layer-3 addresses assigned: %s.' % l3_addrs,
                solution
            )
        else:
            self.res['l3_addrs'] = PositiveOutcome('No Layer-3 addresses assigned to the interface')

    def __repr__(self):
        return '<InterfaceCheck<iface=%s, res=%s>' % (self.iface, self.res)

ifaces = ['eth5', 'eth6']
for iface in ifaces:
    print iface_status(iface)
    ic = IfaceMitmSuitabilityCheck(iface)
    ic.run()
    print ic
