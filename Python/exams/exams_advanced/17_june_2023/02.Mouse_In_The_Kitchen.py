def is_valid(value, max_value):
    return 0 <= value <= max_value - 1


def next_move(current_command, current_row, current_col):
    if current_command == 'up' and is_valid(current_row - 1, N):
        return current_row - 1, current_col
    if current_command == 'down' and is_valid(current_row + 1, N):
        return current_row + 1, current_col
    if current_command == 'left' and is_valid(current_col - 1, M):
        return current_row, current_col - 1
    if current_command == 'right' and is_valid(current_col + 1, M):
        return current_row, current_col + 1
    return None, None


N, M = [int(dimension) for dimension in input().split(',')]

matrix = []
mouse_position = []
cheese = 0

directions = {
    "left": (0, -1),
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
}

for row in range(N):
    line = [symbol for symbol in input()]
    matrix.append(line)
    for symbol in line:
        if symbol == 'M':
            mouse_position = [row, line.index('M')]
        elif symbol == 'C':
            cheese += 1

cheese_eaten = 0
command = input()
while command != "danger":

    mouse_row, mouse_col = mouse_position
    next_row, next_col = next_move(command, mouse_row, mouse_col)

    if next_row is None or next_col is None:
        print("No more cheese for tonight!")
        break

    elif matrix[next_row][next_col] == '@':  # if wall
        command = input()
        continue

    elif matrix[next_row][next_col] == 'T':  # if trap
        matrix[mouse_row][mouse_col] = '*'
        matrix[next_row][next_col] = 'M'
        print("Mouse is trapped!")
        break

    elif matrix[next_row][next_col] == '*':  # if empty
        matrix[mouse_row][mouse_col] = '*'
        matrix[next_row][next_col] = 'M'
        mouse_position = [next_row, next_col]

    elif matrix[next_row][next_col] == 'C':
        cheese_eaten += 1
        matrix[mouse_row][mouse_col] = '*'
        matrix[next_row][next_col] = 'M'
        if cheese_eaten == cheese:
            print("Happy mouse! All the cheese is eaten, good night!")
            break
        mouse_position = [next_row, next_col]

    command = input()

if command == 'danger':
    print("Mouse will come back later!")

for line in matrix:
    print(*line, sep='')
