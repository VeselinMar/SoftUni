from Python.oop.Inheritance.exercise.NeedForSpeed.car import Car


class FamilyCar(Car):

    def __init__(self, fuel, horsepower):
        super().__init__(fuel, horsepower)
