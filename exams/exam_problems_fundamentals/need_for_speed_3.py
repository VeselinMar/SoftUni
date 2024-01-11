def drive(car: str, distance: int, fuel: int):
    if fuel > cars[car]["tank"]:
        print("Not enough fuel to make that ride")
    else:
        cars[car]["mileage"] += distance
        cars[car]["tank"] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")


def refuel(car: str, fuel: int):
    tank_capacity = 75
    if cars[car]["tank"] + fuel > tank_capacity:
        print(f"{car} refueled with {tank_capacity - cars[car]['tank']} liters")
        cars[car]["tank"] = tank_capacity
    else:
        cars[car]["tank"] += fuel
        print(f"{car} refueled with {fuel} liters")


def revert(car: str, kilometers: int):
    minimum = 10000
    if cars[car]["mileage"] - kilometers < 10000:
        cars[car]["mileage"] = 10000
    else:
        cars[car]["mileage"] -= kilometers
        print(f"{car} mileage decreased by {kilometers} kilometers")


n = int(input())  # number of obtainable cars

cars = {}  # create empty dictionary where I can park my cars
for _ in range(n):  # add cars to my dictionary
    car_info = input().split("|")
    key = car_info[0]
    mileage = int(car_info[1])
    tank = int(car_info[2])

    cars[key] = {"mileage": mileage, "tank": tank}

command = input()  # perform actions with my cars
while command != "Stop":
    command = command.split(" : ")
    command_phrase = command[0]
    car = command[1]
    if command_phrase == "Drive":
        distance = int(command[2])
        fuel = int(command[3])
        drive(car, distance, fuel)
        if cars[car]["mileage"] >= 100000:
            cars.pop(car)
            print(f"Time to sell the {car}!")
    elif command_phrase == "Refuel":
        fuel = int(command[2])
        refuel(car, fuel)
    elif command_phrase == "Revert":
        kilometers = int(command[2])
        revert(car, kilometers)

    command = input()

for car in cars:
    print(f'{car} -> Mileage: {cars[car]["mileage"]} kms, Fuel in the tank: {cars[car]["tank"]} lt.')
