import math
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return math.pi * self.__radius ** 2

    def calculate_perimeter(self):
        return math.pi * self.__radius * 2


class Rectangle(Shape):
    def __init__(self, w, h):
        self.__w = w
        self.__h = h

    def calculate_area(self):
        return self.__h * self.__w

    def calculate_perimeter(self):
        return self.__h * 2 + self.__w * 2


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
