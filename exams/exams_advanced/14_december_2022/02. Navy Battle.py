def next_move(command, current_row, current_col):
    if command == 'up':
        return current_row - 1, current_col
    if command == 'down':
        return current_row + 1, current_col
    if command == 'left':
        return current_row, current_col - 1
    if command == 'right':
        return current_row, current_col + 1


n = int(input())

line = ''
matrix = []
submarine = []
for row in range(n):
    line = [el for el in input()]
    if 'S' in line:
        submarine = [row, line.index("S")]
    matrix.append(line)

hits = 0
lives = 3
while line:
    line = input()
    current_row, current_col = submarine
    next_row, next_col = next_move(line, current_row, current_col)

    if matrix[next_row][next_col] == "-":
        matrix[current_row][current_col] = "-"
        submarine = [next_row, next_col]
        matrix[next_row][next_col] = "S"
    elif matrix[next_row][next_col] == "*":
        matrix[current_row][current_col] = "-"
        submarine = [next_row, next_col]
        matrix[next_row][next_col] = "S"
        lives -= 1
        if lives == 0:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{next_row}, {next_col}]!")
            break
    elif matrix[next_row][next_col] == "C":
        matrix[current_row][current_col] = "-"
        submarine = [next_row, next_col]
        matrix[next_row][next_col] = "S"
        hits += 1
        if hits == 3:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

for row in matrix:
    print(*row, sep='')
