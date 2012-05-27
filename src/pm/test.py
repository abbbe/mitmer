import itertools

import src.nm

GLITCHES = [0, 0, 1, 0, 0, 1, 1, 1]

class MyGlitchyBitItem(nm.Item):

	def __init__(self):
		self.glitch_iter = itertools.chain.from_iterable(GLITCHES)

	def check(self):
		# don't capture StopIteration exception on purpose
		return self.glitch_iter.next()

class MyGlitchyBitPolicy(nm.Policy):
	'''
	This policy verifies that the glitchy bit glitches as expected.
	'''
	def __init__(self):
		items = [MyGlitchyBitPolicy()]
		self.glitch_iter = itertools.chain.from_iterable(GLITCHES)
		nm.Policy.__init__(self, items)

	def check(self):
		try:
			return self.glitch_iter.next()
		except StopIteration:
			return nm.ItemCheckResult.

p = MyGlitchyBitPolicy()
assert(p.check()) for i in range(1, len(GLITCHES))

