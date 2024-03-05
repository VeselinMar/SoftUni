from Pizza_Maker.dough import Dough
from Pizza_Maker.topping import Topping


class Pizza:
    def __init__(self, name, dough, max_number_of_toppings):
        if max_number_of_toppings <= 0 or not isinstance(max_number_of_toppings, int):
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        if name == '' or not isinstance(name, str):
            raise ValueError("The name cannot be an empty string")
        if not dough or not isinstance(dough, Dough):
            raise ValueError("You should add dough to the pizza")
        self.__name = name
        self.__dough = dough
        self.__max_number_of_toppings = max_number_of_toppings
        self.__toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, dough: Dough):
        self.__dough = dough

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, num):
        self.__max_number_of_toppings = num

    @property
    def toppings(self):
        return self.__toppings

    @toppings.setter
    def toppings(self, topping: Topping):
        self.__toppings[topping.topping_type] = topping.weight

    # Methods - add_topping & calculate_total_weight

    def add_topping(self, topping: Topping):
        if len(self.__toppings) >= self.max_number_of_toppings:
            raise ValueError("Not enough space for another topping")

        if topping.topping_type in self.__toppings:
            self.__toppings[topping.topping_type] += topping.weight
        else:
            self.__toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        toppings_weight = sum(weight for weight in self.__toppings.values())
        total_weight = self.__dough.weight + toppings_weight
        return total_weight
