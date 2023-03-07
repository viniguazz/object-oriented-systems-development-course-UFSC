
# Intro 

Object: a computational representation of a certain entity, geared towards executing a certain task, with well defined limits. It's a collection of data (attributes) and operations (methods) that operate the data, representing a logic entity in the system.

Abstraction: identify the important aspects of a phenomenon and ignore it's details.

Class: the defition of a group of objects with common properties and behaviours. 

An object is an instatiation of a class.

Attributes are variables that describe an object. Methods are functions (for the imperative paradigm) that operate over an object.

# Declaring classes in Python

class Car:

	def __init__(self, model: str, color: str, licensePlate: str):      # constructor method
		self.model = model
		self.color = color
		self.licensePlate = licensePlate
		self.speed = 0

	def honk(self):
		print('car', self.model, 'honked')

	def accelerate(self):
		self.speed += 10

	def brake(self):
		self.speed -= 10
		if self.speed < 0:
			self.speed = 0

self: is a reference to the object that will be instantiated. It's mandatory and must always be the first argument of any method.
constructor: a method that is automatically triggered whenever a class is instantiated.

# Instantiation

	def main():
		car1 = Car('Gol', 'red', 'LCC-555')

		car.honk()
		car.accelerate()

Attention: notice that SELF isn't passed whenever the methods of an instantiated object are called.

# Pillars of abstraction


