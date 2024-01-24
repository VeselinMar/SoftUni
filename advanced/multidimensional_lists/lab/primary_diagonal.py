N = int(input())

matrix_diagonal = 0
matrix = []
for row in range(N):
    line = [int(num) for num in input().split()]
    matrix_diagonal += line[row]

print(matrix_diagonal)
