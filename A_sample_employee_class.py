import sys
print(sys.executable)
print(sys.version)

class Name:

	"""A sample Name Class """

	def __init__(self, first, last):
		self.first = first
		self.last = last

name_1 = Name('Jean', 'Pereira')

print(name_1.first)
print(name_1.last)
