from Python.oop.Inheritance.exercise.NeedForSpeed.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):

    DEFAULT_FUEL_CONSUMPTION = 8

    def __init__(self, fuel, horsepower):
        super().__init__(fuel, horsepower)

