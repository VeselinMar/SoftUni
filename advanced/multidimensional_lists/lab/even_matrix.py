rows = int(input())

even_matrix = []
for _ in range(rows):
    row = [int(num) for num in input().split(', ') if int(num) % 2 == 0]
    even_matrix.append(row)

print(even_matrix)
