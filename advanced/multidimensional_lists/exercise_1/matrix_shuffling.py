r, c = [int(num) for num in input().split()]

matrix = []
for _ in range(r):
    row = [num for num in input().split()]
    matrix.append(row)

command = input()
while command != 'END':
    command = command.split()

    if command[0] == 'swap' and len(command) == 5:
        row1, col1, row2, col2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])
        if row1 > r - 1 or col1 > c - 1 or row2 > r - 1 or col2 > c - 1:
            print('Invalid input!')
        elif row1 < 0 or col1 < 0 or row2 < 0 or col2 < 0:
            print('Invalid input!')

        else:
            a = matrix[row1][col1]
            b = matrix[row2][col2]
            matrix[row1][col1] = b
            matrix[row2][col2] = a
            for line in matrix:
                print(*line)

    else:
        print('Invalid input!')

    command = input()
