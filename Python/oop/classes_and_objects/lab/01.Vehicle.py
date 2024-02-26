class Vehicle:

    def __init__(self, mileage, max_speed=None):
        self.max_speed = max_speed if max_speed is not None else 150
        self.mileage = mileage
        self.gadgets = []


car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)
