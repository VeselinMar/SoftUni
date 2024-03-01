from Python.oop.Inheritance.exercise.Shop.product import Product


class Food(Product):

    def __init__(self, name, quantity: int = 15):
        super().__init__(name, quantity)
