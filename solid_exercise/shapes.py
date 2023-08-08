from abc import ABC, abstractmethod


class AlgebraFigure(ABC):
    @abstractmethod
    def area_formula(self):
        pass


class Rectangle(AlgebraFigure):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_formula(self):
        return self.width * self.height


class Triangle(AlgebraFigure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_formula(self):
        return (self.width * self.height) / 2


class AreaCalculator:

    def __init__(self, shapes):
        self.shapes = shapes

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        if not isinstance(shapes, list):
            raise ValueError("`shapes` should be of type `list`.")
        self.__shapes = value

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.area_formula()

        return total


# FILE TEST

shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
