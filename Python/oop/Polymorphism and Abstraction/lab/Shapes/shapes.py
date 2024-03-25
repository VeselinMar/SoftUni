from abc import ABC, abstractmethod
import math


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
        area = math.pi * self.__radius ** 2
        return area

    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.__radius
        return perimeter


class Rectangle(Shape):

    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def calculate_area(self):
        area = self.__width * self.__height
        return area

    def calculate_perimeter(self):
        perimeter = 2 * (self.__width + self.__height)
        return perimeter


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
