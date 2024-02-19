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

matrix = []
jet_fighter = []

for row in range(N):
    line = [el for el in input()]
    if "J" in line:
        jet_fighter = [row, line.index("J")]
    matrix.append(line)

shot_down = 0
enemies = 4
armor = 300
while True:
    line = input()
    current_row, current_col = jet_fighter
    next_row, next_col = next_move(line, current_row, current_col)

    if next_row is None or next_col is None:
        continue

    elif matrix[next_row][next_col] == "-":
        jet_fighter = [next_row, next_col]
        matrix[next_row][next_col] = "J"
        matrix[current_row][current_col] = "-"

    elif matrix[next_row][next_col] == "E":

        if shot_down == 3:
            matrix[next_row][next_col] = "J"
            matrix[current_row][current_col] = "-"
            shot_down += 1
            print("Mission accomplished, you neutralized the aerial threat!")
            break

        else:
            matrix[current_row][current_col] = "-"
            matrix[next_row][next_col] = "J"
            armor -= 100
            if armor == 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates"
                      f" [{next_row}, {next_col}]!")
                break
            shot_down += 1
            jet_fighter = [next_row, next_col]

    elif matrix[next_row][next_col] == "R":
        jet_fighter = [next_row, next_col]
        armor = 300
        matrix[next_row][next_col] = "J"
        matrix[current_row][current_col] = "-"

for row in matrix:
    print(*row, sep='')
