from Python.oop.Inheritance.exercise.NeedForSpeed.vehicle import Vehicle


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3.0

    def __init__(self, fuel, horsepower):
        super().__init__(fuel, horsepower)

