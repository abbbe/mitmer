'''
'''
import nm

class MitmBridgeConfig(object):
	'''
	This class holds all configuration items relevant for MITM bridge setup.
	'''
	def __init__(self, addr, gateway, netmask, mac, gwmac, controller, i1, i2):
		self.addr = addr
		self.gateway = gateway
		self.netmask = netmask
		self.mac = mac
		self.gmac = gwmac
		self.controller = controller

		self.i1 = i1
		self.i2 = i2

class MitmerNMPolicy(nm.Policy):
	'''
	This class knows how Linux network stack, interfaces, OVS, etc need to be
	configured to facilitate MITM exercises.
	'''
	def __init__(self, bridge_config):
		self.bridge_config = bridge_config

		self.append_item(nm.mitmer.items.EmptyIptablesPolicy(i))

		self.init_mitm_iface(self.bridge_config.i1)
		self.init_mitm_iface(self.bridge_config.i2)

		self.init_mitm_bridge()

	def init_mitm_iface(self, i):
		self.append_item(nm.mitmer.items.IfaceUp(i))
#		self.append_item(nm.mitmer.items.IfaceNotUnderNM(i))
#
#		self.append_item(nm.mitmer.items.NoIPv6AddrsOnIface(i))
#		self.append_item(nm.mitmer.items.NoL3AddrsOnIface(i))
#		self.append_item(nm.mitmer.items.NoRPFOnIface(i))
#		self.append_item(nm.mitmer.items.NoARPOnIface(i))
#
#		self.append_item(nm.mitmer.items.DropOutput(i))
#
#		self.append_item(nm.mitmer.items.IfaceLinkDetected(i))
#		self.append_item(nm.mitmer.items.IfaceFullDuplex(i))
#		self.append_item(nm.mitmer.items.IfaceNoErrors(i))
#
#		self.init_mitm(i)

	def init_mitm_bridge(self):
		self.append_item(nm.mitmer.items.MitmBridge(i, self.bridge_config))

