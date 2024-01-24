N = int(input())

matrix = []
for _ in range(N):
    row = [el for el in input()]
    matrix.append(row)

symbol = input()
found = False
for row in range(len(matrix)):
    if found:
        break
    for column in range(len(matrix[row])):
        if symbol == matrix[row][column]:
            print(f'({row}, {column})')
            found = True
            break

if not found:
    print(f'{symbol} does not occur in the matrix')
