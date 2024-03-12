from project.animals.animal import Mammal
from project.animals.birds import Hen, Owl
from project.food import Meat, Vegetable, Fruit


class Mouse(Mammal):

    @property
    def edible_food(self):
        return [Vegetable, Fruit]

    @property
    def gained_weight(self):
        return 0.10

    @staticmethod
    def make_sound():
        return "Squeak"


class Dog(Mammal):

    @property
    def edible_food(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.40

    @staticmethod
    def make_sound():
        return "Woof!"


class Cat(Mammal):

    @property
    def edible_food(self):
        return [Vegetable, Meat]

    @property
    def gained_weight(self):
        return 0.30

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):

    @property
    def edible_food(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 1.00

    @staticmethod
    def make_sound():
        return "ROAR!!!"


owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)
hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)
