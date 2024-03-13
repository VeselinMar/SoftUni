from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    def get_species(self):
        return f"{self.name} is a {self.__class__.__name__}."

    @abstractmethod
    def animal_sound(self):
        pass


class Dog(Animal):

    def animal_sound(self):
        return f"{self.name} says 'Woof - woof!'"


class Cat(Animal):

    def animal_sound(self):
        return f"{self.name} says 'Meow!'"


class Pig(Animal):

    def animal_sound(self):
        return f"{self.name} says 'Oink!'"


animals = [Dog("Johny"), Cat('Robert'), Pig('Sam')]
for animal in animals:
    print(animal.animal_sound())
