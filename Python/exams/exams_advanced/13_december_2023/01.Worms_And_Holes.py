from collections import deque

worms = [int(worm) for worm in input().split()]
holes = deque([int(hole) for hole in input().split()])

dead_worms = 0
matches = 0
while worms and holes:
    worm = worms.pop()
    hole = holes.popleft()
    if worm != hole:
        worm -= 3
        if worm > 0:
            worms.append(worm)
        else:
            dead_worms += 1
    else:
        matches += 1

if matches:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worms:
    if not dead_worms:
        print("Every worm found a suitable hole!")
    else:
        print("Worms left: none")
else:
    print("Worms left: ", end='')
    print(*worms, sep=', ')

if not holes:
    print("Holes left: none")
else:
    print("Holes left: ", end='')
    print(*holes, sep=', ')
