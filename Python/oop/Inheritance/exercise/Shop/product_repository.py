from Python.oop.Inheritance.exercise.Shop.drink import Drink
from Python.oop.Inheritance.exercise.Shop.food import Food
from Python.oop.Inheritance.exercise.Shop.product import Product


class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name: str):
        product_to_remove = self.find(product_name)
        if product_to_remove:
            self.products.remove(product_to_remove)

    def __repr__(self):
        return_string = "\n".join([f"{product.name}: {product.quantity}" for product in self.products])
        return return_string


food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)
