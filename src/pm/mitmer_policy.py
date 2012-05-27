'''
This is a sample implementation of policy.
'''

class MitmerNMPolicy(nm.Policy):
	def __init__(self, i1, i2, bridge_config):
		self.i1 = i1
		self.i2 = i2
		self.bridge_config = bridge_config

		self.init_mitm_iface(self.i1)
		self.init_mitm_iface(self.i2)
		self.init_mitm_bridge()

	def init_mitm_iface(self, i):
		self.items.append(nm.items.NotUnderNM(i))
		self.items.append(nm.items.NoIPv6(i))
		self.items.append(nm.items.NoL3Addresses(i))
		self.items.append(nm.items.DropOutput(i))
		self.items.append(nm.items.NoRPF(i))
		self.init_mitm(self, i):

	def init_mitm_bridge(self):
		self.items.append(nm.items.MitmBridge(i, self.bridge_config))

# ---

i1 = 'vmnet1'
i2 = 'vmnet8'

bc = MitmBridgeConfig(
	addr = IpAddr('10.255.255.254'),
	gateway = IpAddr('10.255.255.253'),
	netmask = IpAddr('255.255.255.252'),
	mac = EthAddr('55:55:55:55:55'),  # FIXME
	gwmac = EthAddr('aa:aa:aa:aa:aa')  # FIXME
)

controller = 'tcp:localhost:6633'

p = MitmerNMPolicy(i1, i2, bc, controller)
p.run()

