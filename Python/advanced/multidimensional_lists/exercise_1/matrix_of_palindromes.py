r, c = [int(num) for num in input().split()]

first = 97
matrix = []
for row in range(r):
    line = []

    for column in range(c):
        l1 = chr(first + row)
        l2 = chr(first + row + column)
        l3 = l1

        line.append(l1 + l2 + l3)

    matrix.append(line)

for row in matrix:
    print(*row, sep=' ')
