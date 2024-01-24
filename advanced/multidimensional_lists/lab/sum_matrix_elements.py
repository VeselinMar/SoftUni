rows, columns = [int(num) for num in input().split(', ')]

matrix_sum = 0
matrix = []
for _ in range(rows):
    row = [int(num) for num in input().split(', ')]
    matrix.append(row)
    matrix_sum += sum(row)

print(matrix_sum)
print(matrix)
