rows, columns = [int(num) for num in input().split()]

matrix = []
for _ in range(rows):
    row = [int(el) for el in input().split()]
    matrix.append(row)

max_sum_of_cells = 0
largest_subset = []
for row in range(rows - 2):
    for column in range(columns - 2):
        a = matrix[row][column]
        a1 = matrix[row][column+1]
        a2 = matrix[row][column+2]
        b = matrix[row+1][column]
        b1 = matrix[row+1][column+1]
        b2 = matrix[row+1][column+2]
        c = matrix[row+2][column]
        c1 = matrix[row+2][column+1]
        c2 = matrix[row + 2][column + 2]
        sum_of_cells = a+a1+a2+b+b1+b2+c+c1+c2
        if sum_of_cells > max_sum_of_cells:
            largest_subset.clear()
            max_sum_of_cells = sum_of_cells
            largest_subset.append([a, a1, a2])
            largest_subset.append([b, b1, b2])
            largest_subset.append([c, c1, c2])

print(f'Sum = {max_sum_of_cells}')
for line in largest_subset:
    print(*line)
