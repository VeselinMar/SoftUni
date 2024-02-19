from collections import deque

monsters_armor = deque([int(value) for value in input().split(',')])
strike_strength = [int(value) for value in input().split(',')]

kill_count = 0

while monsters_armor and strike_strength:
    monster = monsters_armor.popleft()
    strike = strike_strength.pop()

    if strike >= monster:
        strike -= monster
        kill_count += 1
        if strike_strength:
            strike_strength[-1] += strike
        elif not strike_strength and strike > 0:
            strike_strength.append(strike)

    else:
        monster -= strike
        monsters_armor.append(monster)

if not monsters_armor:
    print("All monsters have been killed!")
if not strike_strength:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {kill_count}")
