line = input()
cities = {}
while line != "Sail":
    line = line.split("||")
    city, population, gold = line[0], int(line[1]), int(line[2])
    if city not in cities:
        cities[city] = {"people": population, 'gold': gold}
    else:
        cities[city]["people"] += population
        cities[city]["gold"] += gold
    line = input()

while line != "End":
    line = line.split("=>")
    if line[0] == "Plunder":
        city, people, gold = line[1], int(line[2]), int(line[3])
        cities[city]["people"] -= people
        cities[city]["gold"] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[city]["people"] <= 0 or cities[city]["gold"] <= 0:
            del cities[city]
            print(f"{city} has been wiped off the map!")
    elif line[0] == "Prosper":
        city, gold = line[1], int(line[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[city]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")
    line = input()

if cities:
    print(f"Ahoy, Captain! There are {len(cities.keys())} wealthy settlements to go to:")
    for city in cities.keys():
        print(f"{city} -> Population: {cities[city]['people']} citizens, Gold: {cities[city]['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
