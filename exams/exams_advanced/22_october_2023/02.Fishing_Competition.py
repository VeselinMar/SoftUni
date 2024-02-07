def check_move(next_pos, area):
    size = len(area)
    r, c = next_pos

    if r < 0:
        moved = size - 1, c
    elif r >= size:
        moved = 0, c
    elif c < 0:
        moved = r, size - 1
    elif c >= size:
        moved = r, 0
    else:
        moved = next_pos

    return moved


n = int(input())

fisher_position = []
fishing_area = []
tonnes_needed = 20
tonnes_caught = 0
whirlpool = False

for row in range(n):
    line = [s for s in input()]
    if 'S' in line:
        fisher_position = [row, line.index('S')]
    fishing_area.append(line)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

command = input()
while command != "collect the nets":
    r, c = fisher_position
    row, col = directions.get(command)
    next_position = (r + row, c + col)
    move = check_move(next_position, fishing_area)

    if fishing_area[move[0]][move[1]] == '-':
        fishing_area[fisher_position[0]][fisher_position[1]] = '-'
        fisher_position = move[0], move[1]
        fishing_area[fisher_position[0]][fisher_position[1]] = 'S'

    elif fishing_area[move[0]][move[1]] == 'W':
        fisher_position = move[0], move[1]
        tonnes_caught = 0
        whirlpool = True
        break

    else:
        catch = int(fishing_area[move[0]][move[1]])
        fishing_area[fisher_position[0]][fisher_position[1]] = '-'
        fisher_position = move[0], move[1]
        fishing_area[fisher_position[0]][fisher_position[1]] = 'S'
        tonnes_caught += catch

    command = input()

if whirlpool:
    print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught."
          f" Last coordinates of the ship: [{fisher_position[0]},{fisher_position[1]}]")

else:
    if tonnes_caught >= tonnes_needed:
        print("Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {tonnes_needed - tonnes_caught}"
              f" tons of fish more.")

    if tonnes_caught > 0:
        print(f"Amount of fish caught: {tonnes_caught} tons.")

    for line in fishing_area:
        print(''.join(line))
