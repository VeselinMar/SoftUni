rows, columns = [int(num) for num in input().split(', ')]

sub_matrix = []
matrix = []
highest_square = 0
for _ in range(rows):
    row = [int(num) for num in input().split(', ')]
    matrix.append(row)

for row in range(rows - 1):
    for column in range(columns - 1):
        a = matrix[row][column]
        b = matrix[row + 1][column]
        c = matrix[row][column + 1]
        d = matrix[row + 1][column + 1]
        result = a + b + c + d
        if result > highest_square:
            sub_matrix.clear()
            highest_square = result
            sub_matrix.append([a, c])
            sub_matrix.append([b, d])

for line in sub_matrix:
    print(*line)
print(highest_square)
