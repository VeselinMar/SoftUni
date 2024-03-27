n = int(input())

matrix = []
for _ in range(n):
    line = [int(num) for num in input().split()]
    matrix.append(line)

command = input()
while command != 'END':
    command = command.split()
    task, row, col, value = command[0], int(command[1]), int(command[2]), int(command[3])

    if n > row >= 0 and n > col >= 0:
        if task == 'Add':
            matrix[row][col] += value
        elif task == 'Subtract':
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')

    command = input()

for line in matrix:
    print(*line)
