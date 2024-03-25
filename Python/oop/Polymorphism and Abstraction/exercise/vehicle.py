from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):

    FUEL_CONSUMPTION_INCREMENT = 0.9

    def drive(self, distance):
        consumption = self.fuel_consumption + Car.FUEL_CONSUMPTION_INCREMENT
        if self.fuel_quantity - consumption * distance >= 0:
            self.fuel_quantity -= consumption * distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):

    FUEL_CONSUMPTION_INCREMENT = 1.6
    REFUEL_EFFICIENCY = 0.95

    def drive(self, distance):
        consumption = self.fuel_consumption + Truck.FUEL_CONSUMPTION_INCREMENT
        if self.fuel_quantity - consumption * distance >= 0:
            self.fuel_quantity -= consumption * distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel * Truck.REFUEL_EFFICIENCY


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
