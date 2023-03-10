
import inspect


class Shape:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def position(self):
        return (self.x, self.y)
    
    def greeting(self):
        print(f'I\'m a Shape!')


class Circle(Shape):

    def __init__(self, x, y, radius):
        Shape.__init__(self, x, y)
        self.radius = radius

    def getArea(self):
        return self.radius**2
    
    def greeting(self):
        print(f'I\'m a Circle. Also,')
        Shape.greeting(self)


class Rectangle(Shape):
    
    def __init__(self, x: int, y: int, width: int, heigth: int):
        super().__init__(x, y)
        self.width = width
        self.heigth = heigth
    
    def getArea(self):
        return self.width * self.heigth
    
    def greeting(self):
        print(f'I\'m a Rectangle. Also,')
        super().greeting()


class Square(Shape):
    
    def __init__(self, x: int, y: int, side: int):
        super().__init__(x, y)
        self.side = side
    
    def getArea(self):
        return self.side ** 2
    
    def greeting(self):
        print(f'I\'m a Square. Also,')
        super().greeting()


'''
For whatever reason, calling the parent class constructor directly
works just like calling super(). In other words: both the constructor
and the methods are made available to the subclasses.

Whenever you call a mehtod directly from the parent class (without the super()),
you must feed the 'self' keyword as an argument.

Notice we don't use 'self' with super().

It's interesting to use super() because it's easier to alter the classes names 
(since we are not directly calling them inside the subclass member definitions).

The super() built-in returns a proxy object, a substitute object that can call 
methods of the base class via delegation. This is called indirection (ability 
to reference base object with super()).


'''

shape1 = Shape(23, 4)
circle1 = Circle(45, 5, 6)
square1 = Square(5, 4, 10)

shape1.greeting()
circle1.greeting()
square1.greeting()

print()
print()
print('shape1-position: ', shape1.position())
print('circle1-position: ', circle1.position())
print('circle1-area: ', circle1.getArea())
print('square1-position: ', square1.position())
print('square1-area: ', square1.getArea())
print()
print()
print(dir(circle1))
print()
print()
print(inspect.getmembers(circle1))
