rows = int(input())

flattened = []
matrix = []
for _ in range(rows):
    row = [int(num) for num in input().split(', ')]
    matrix.append(row)
    for el in row:
        flattened.append(el)

print(flattened)
