m = int(input())  # number of presents
n = int(input())  # size of matrix

matrix = []
santa_cell = []
to_deliver = 0
nice = 0

for row in range(n):
    line = [symbol for symbol in input().split()]
    for cell in line:
        if cell == 'S':
            santa_cell = [row, line.index('S')]
        elif cell == 'V':
            to_deliver += 1
            nice += 1
    matrix.append(line)

moves = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

command = input()
while command != 'Christmas morning':
    r, c = santa_cell
    row, col = moves.get(command)
    next_position = [r + row, c + col]

    if matrix[next_position[0]][next_position[1]] == 'X':
        matrix[santa_cell[0]][santa_cell[1]] = '-'
        santa_cell = next_position

    elif matrix[next_position[0]][next_position[1]] == '-':
        matrix[santa_cell[0]][santa_cell[1]] = '-'
        santa_cell = next_position
        matrix[next_position[0]][next_position[1]] = 'S'

    elif matrix[next_position[0]][next_position[1]] == 'V':
        m -= 1
        matrix[santa_cell[0]][santa_cell[1]] = '-'
        santa_cell = next_position
        matrix[next_position[0]][next_position[1]] = 'S'
        to_deliver -= 1

    elif matrix[next_position[0]][next_position[1]] == 'C':
        matrix[santa_cell[0]][santa_cell[1]] = '-'
        santa_cell = next_position
        row, col = santa_cell[0], santa_cell[1]
        matrix[next_position[0]][next_position[1]] = 'S'
        for direction in moves:
            r, c = moves.get(direction)
            neighbour_cell = [r + row, c + col]
            if matrix[neighbour_cell[0]][neighbour_cell[1]] == 'X':
                m -= 1
                matrix[neighbour_cell[0]][neighbour_cell[1]] = '-'
            elif matrix[neighbour_cell[0]][neighbour_cell[1]] == 'V':
                m -= 1
                to_deliver -= 1
                matrix[neighbour_cell[0]][neighbour_cell[1]] = '-'
            if m == 0:
                break
    if m == 0:
        break
    command = input()

if not m and to_deliver:
    print('Santa ran out of presents!')

for line in matrix:
    print(*line)

if not to_deliver:
    print(f"Good job, Santa! {nice} happy nice kid/s.")
else:
    print(f"No presents for {to_deliver} nice kid/s.")
