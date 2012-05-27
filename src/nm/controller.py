
#import sys
#sys.path.insert(0, '..')
#
#import nm
#import logging
#
#i1 = 'vmnet1'
#i2 = 'vmnet8'
#
#logger = logging.getLogger('nm')
#
#bc = nm.MitmBridgeConfig(
#	addr=IpAddr('10.255.255.254'),
#	gateway=IpAddr('10.255.255.253'),
#	netmask=IpAddr('255.255.255.252'),
#	mac=EthAddr('55:55:55:55:55'), # FIXME
#	gwmac=EthAddr('aa:aa:aa:aa:aa')  # FIXME
#)
#controller = 'tcp:localhost:6633'
#p = nm.mitmer.MitmerNMPolicy(i1, i2, bc, controller)
#threading.Thread(target=p.run).start()
