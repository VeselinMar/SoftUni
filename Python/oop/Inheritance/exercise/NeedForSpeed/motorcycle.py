from Python.oop.Inheritance.exercise.NeedForSpeed.vehicle import Vehicle


class Motorcycle(Vehicle):

    def __init__(self, fuel, horsepower):
        super().__init__(fuel, horsepower)
