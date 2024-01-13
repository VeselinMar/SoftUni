from collections import deque


# define a function to check if fuel is enough to cover distance
def can_reach_destination(fuel: int, distance: int):
    if fuel >= distance:
        return True
    else:
        return False


number_of_petrol_pumps = int(input())
fuel = 0
# initiate a deck with stops and add items to deck
stops = deque()
for pump in range(number_of_petrol_pumps):
    line = list(map(int, input().split()))
    stops.append(line)
# find the correct starting point by rotating the deck if needed
count = 0
found = False
while found is False:
    inner_count = 0
    for item in stops:
        amount, distance = item[0], item[1]
        fuel += amount
        if not can_reach_destination(fuel, distance):
            stops.rotate(-1)
            count += 1
            fuel = 0
            break
        fuel -= distance
        inner_count += 1
        if inner_count == len(stops):
            found = True
print(count)
