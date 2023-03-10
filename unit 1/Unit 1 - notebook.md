
# Intro 

OOP is a method that aims to organize the code in a way that get closer to real world.

* Object: a computational representation of a certain entity, geared towards executing a certain task, with well defined limits. It's a collection of data (attributes) and operations (methods) that operate the data, representing a logic entity in the system.

* Abstraction: identify the important aspects of a phenomenon and ignore it's details.

* Class: the defition of a group comprised of objects that share common properties and behaviors. 

An object is an instatiation of a class.

Attributes are variables that describe an object. Methods are functions (for the imperative paradigm) that operate over an object.

### Declaring classes in Python

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

The 'self' keyword is a reference to the object that will be instantiated. It's mandatory and must always be the first argument of any method.

The 'constructor' is a method that is automatically triggered whenever a class is instantiated.

### Instantiation

	def main():
		car1 = Car('Gol', 'red', 'LCC-555')

		car.honk()
		car.accelerate()

Attention: notice that SELF isn't passed whenever the methods of an instantiated object are called. Notice that we use dot notation.

### Pillars of abstraction

* Encapsulation
* Inheritance
* Composition
* Polymorphism

# Inheritance

It's a mechanism that allows reuse of implemented code. It defines a relationship between classes, in which we verify what's common.
Classes share their structure/behaviors. It's a specialization/generalization relationship.

Note: private attributes are preceded by two underscores in python.

Note2: decorators

	In Python syntax, the "@" symbol is used as a decorator in Object-Oriented Programming (OOP) to modify the behavior of a function or method.

	A decorator is a special type of function that takes another function as an argument and extends the behavior of the latter function without modifying its source code. Decorators are identified by the "@" symbol, which is followed by the name of the decorator function.

	Here's an example of how the "@" symbol is used in Python syntax to create a decorator:

		def my_decorator(func):
		    def wrapper():
		        print("Something is happening before the function is called.")
		        func()
		        print("Something is happening after the function is called.")
		    return wrapper

		@my_decorator
		def say_hello():
		    print("Hello!")

		say_hello()

	In the code above, we defined a decorator function called my_decorator that takes a function func as an argument and returns a new function called wrapper. The wrapper function is then used to wrap the original say_hello function by applying the @my_decorator decorator to it.

	When the say_hello function is called, it is actually the wrapper function that is executed, which adds some extra behavior before and after the original function call.



