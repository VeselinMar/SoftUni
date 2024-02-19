def is_valid(value, max_value):
    return 0 <= value < max_value


def next_move(command, current_row, current_col):
    if command == 'up' and is_valid(current_row - 1, N):
        return current_row - 1, current_col
    if command == 'down' and is_valid(current_row + 1, N):
        return current_row + 1, current_col
    if command == 'left' and is_valid(current_col - 1, N):
        return current_row, current_col - 1
    if command == 'right' and is_valid(current_col + 1, N):
        return current_row, current_col + 1
    return None, None


N = int(input())

direction_commands = input().split(', ')

matrix = []
squirrel = []
for row in range(N):
    line = [symbol for symbol in input()]
    matrix.append(line)
    if 's' in line:
        squirrel = (row, line.index('s'))

directions = {
    "left": (0, -1),
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
}
hazelnuts_collected = 0
dead = False

for direction in direction_commands:
    row, col = squirrel
    next_row, next_col = next_move(direction, row, col)
    if next_row is None or next_col is None:
        print("The squirrel is out of the field.")
        dead = True
        break

    elif matrix[next_row][next_col] == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        dead = True
        break

    elif matrix[next_row][next_col] == 'h':
        matrix[next_row][next_col] = '*'
        hazelnuts_collected += 1
        if hazelnuts_collected == 3:
            print("Good job! You have collected all hazelnuts!")
            break

    squirrel = [next_row, next_col]

if hazelnuts_collected < 3 and not dead:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts_collected}")
