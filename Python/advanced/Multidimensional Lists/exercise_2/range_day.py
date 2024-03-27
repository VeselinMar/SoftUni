matrix = []

shooter = []
targets = []
total_targets = 0
for row in range(5):
    line = [symbol for symbol in input().split()]
    if 'A' in line:
        shooter = [row, line.index('A')]
    for s in line:
        if s == 'x':
            total_targets += 1
    matrix.append(line)

moves = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

n = int(input())

for _ in range(n):
    line_input = input().split()

    if len(line_input) == 3:  # move
        r, c = shooter[0], shooter[1]
        direction, steps = line_input[1], int(line_input[2])
        row, col = moves.get(direction)
        next_position = (r + (row * steps), c + (col * steps))

        if 0 > next_position[0] or 0 > next_position[1] or next_position[0] > 4 or next_position[1] > 4:
            continue

        elif matrix[next_position[0]][next_position[1]] != '.':
            continue

        else:
            shooter = [next_position[0], next_position[1]]

    else:  # shoot
        count = 1
        r, c = shooter[0], shooter[1]
        direction = line_input[1]
        row, col = moves.get(direction)
        target = [r + row * count, c + col * count]
        while not (0 > target[0] or 0 > target[1] or target[0] > 4 or target[1] > 4):
            if matrix[target[0]][target[1]] == 'x':
                targets.append(target)
                matrix[target[0]][target[1]] = '.'
                break
            else:
                count += 1
                target = [r + row * count, c + col * count]
        if len(targets) == total_targets:
            break

if len(targets) == total_targets:
    print(f"Training completed! All {total_targets} targets hit.")

else:
    print(f"Training not completed! {total_targets - len(targets)} targets left.")

for target in targets:
    print(target)
