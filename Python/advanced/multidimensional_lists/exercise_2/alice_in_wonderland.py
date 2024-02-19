n = int(input())

moves = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

quantity = 0
alice_position = []
matrix = []

for row in range(n):
    line = [symbol for symbol in input().split()]
    if 'A' in line:
        alice_position = [row, line.index('A')]
    matrix.append(line)

fallen = False

while quantity < 10:
    r, c = alice_position[0], alice_position[1]
    command = input()
    row, col = moves.get(command)
    next_position = (r + row, c + col)

    if 0 > next_position[0] or next_position[0] >= n or 0 > next_position[1] or next_position[1] >= n:
        matrix[alice_position[0]][alice_position[1]] = '*'
        fallen = True
        break
    elif matrix[next_position[0]][next_position[1]] == 'R':
        matrix[next_position[0]][next_position[1]] = '*'
        matrix[alice_position[0]][alice_position[1]] = '*'
        fallen = True
        break
    elif matrix[next_position[0]][next_position[1]] == '.' or matrix[next_position[0]][next_position[1]] == '*':
        matrix[alice_position[0]][alice_position[1]] = '*'
        alice_position = [next_position[0], next_position[1]]
    else:
        quantity += int(matrix[next_position[0]][next_position[1]])
        matrix[alice_position[0]][alice_position[1]] = '*'
        alice_position = [next_position[0], next_position[1]]
        if quantity >= 10:
            matrix[next_position[0]][next_position[1]] = '*'

if fallen:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

for line in matrix:
    print(*line)
