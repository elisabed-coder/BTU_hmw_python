import math


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return None


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


def print_area(shape):
    print(f"{shape.name} area: {shape.area()}")

# Instantiate objects


rectangle = Rectangle('Rectangle', 4, 5)
circle = Circle('circle', 3)

print_area(rectangle)
print_area(circle)
