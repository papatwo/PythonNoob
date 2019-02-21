class Parent():
	def __init__(self, last_name, eye_colour):
		print('parent constructor called')
		self.last_name = last_name
		self.eye_colour = eye_colour

class Child(Parent):
	def __init__(self, last_name, eye_colour, no_toys):
		Parent.__init__(self, last_name, eye_colour)
		self.no_toys = no_toys

billy_cyrus = Parent('Cyrus','blue')
print(billy_cyrus.last_name)
miley_cyrus = Child('Cyrus','blue','5')
print(miley_cyrus.no_toys)