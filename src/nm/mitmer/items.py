from nm import stack

def sudo(cmd):
	pass

class IfaceUp(IfaceItem):
	def check(self):
		return stack.get_iface(self.iface).up

	def fix(self):
		sudo(['ip', 'link', self.iface, 'up'])

class IfaceNotUnderNM(IfaceItem):
	def check(self):
		return stack.get_iface(self.iface).under_nm

	def fix(self):
		sudo(['ifdown', self.iface])

class NoIPv6AddrsOnIface(IfaceItem): pass
	def check(self):
		return stack.get_iface(self.iface).under_nm

	def fix(self):
		sudo(['ifdown', self.iface])

class NoL3AddrsOnIface(IfaceItem): pass
	def check(self):
	def fix(self):

class DropIfaceOutput(IfaceItem): pass
class NoRPFOnIface(IfaceItem): pass
class MitmBridge(IfaceItem): pass

class IfaceLinkDetected(IfaceItem): pass
class IfaceFullDuplex(IfaceItem): pass
class IfaceNoErrors(IfaceItem): pass

class EmptyIptablesPolicy(Item): pass


links = Links()
