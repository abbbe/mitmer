'''
Network Manager module.

* The purpose of this module is to set and monitor the configuration OS network stack and network interfaces.
* For example, it helps enforcing network configuration required for mitmer.
* After configuration is set, this module concontinuously monitors applied settings and to make sure they remain in a correct state.
* Target network interfaces, L2/L3 addresses of tap interface are specified provided on startup or can be changed in run-time.
* All identified configuration deviations and corrective actions are logged.


The most important abstract classes are Item, Action, and Policy.
* Conrete item classes carry data necessary to perform a configuration check.
* A concrete policys know enough to validate items it supports and produce events
indicating item state changes. It also knows what actions need to be taken to remedy
the problem.

about
produce config informational events, config mismatch events,
action start event, action end event, action failure

'''

# ----------------------------------------------------

class Item(object):
	'''
	This is an abstract item the module works with. Subclasses of this class 
	get instantiated during policy initialization and updates. They are expected
	to contain necessary configuration information, and state to 
	'''
	def check(self):
		'''
		Subclasses must implement this method to check the 
		'''
		raise NotImplemented()


class ItemCheckResult(object):
	pass

# ----------------------------------------------------

class InterfaceItem(Item):
	def __init__(self, name):
		self.name = iface_name

# ----------------------------------------------------

class Policy(object):
	def __init__(self, items):
		self.items = items

	def get_items_iterator(self):
		return self.items.__iterator__()

# ----------------------------------------------------

class MitmTapConfig(object):
	def __init__(self, name = 'mitm0', host_ip4addr='10.255.255.254', netmask='255.255.255.252', gw_ip4addr='10.255.255.253', host_macaddr='', gw_macaddr=''):
		pass


class PortManager(object):
	def __init__(self, mitm_iface_name1, mitm_iface_name2, tap_config):
		pass

	def start(self):
		pass

	def stop(self):
		pass

