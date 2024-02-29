from Python.oop.Inheritance.exercise.NeedForSpeed.car import Car


class SportCar(Car):

    DEFAULT_FUEL_CONSUMPTION = 10

    def __init__(self, fuel, horsepower):
        super().__init__(fuel, horsepower)

