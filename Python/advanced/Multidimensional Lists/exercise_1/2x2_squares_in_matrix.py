rows, columns = [int(num) for num in input().split()]

matrix = []
for _ in range(rows):
    row = [el for el in input().split()]
    matrix.append(row)

found = 0
for row in range(rows - 1):
    for column in range(columns - 1):
        a = matrix[row][column]
        b = matrix[row+1][column]
        c = matrix[row][column+1]
        d = matrix[row+1][column+1]
        if a == b and b == c and c == d:
            found += 1

print(found)
