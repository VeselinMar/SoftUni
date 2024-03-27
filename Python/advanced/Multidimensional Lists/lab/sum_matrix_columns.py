rows, columns = [int(num) for num in input().split(', ')]

matrix = []
for _ in range(rows):
    row = [int(num) for num in input().split()]
    matrix.append(row)

column_sum = 0
for column in range(columns):
    for row in range(len(matrix)):
        column_sum += matrix[row][column]
    print(column_sum)
    column_sum = 0
