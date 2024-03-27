N = int(input())


primary_diagonal = []
secondary_diagonal = []
for count in range(N):
    row = [int(num) for num in input().split(', ')]
    primary_diagonal.append(row[count])
    row.reverse()
    secondary_diagonal.append(row[count])

print('Primary diagonal: ', end='')
print(*primary_diagonal, sep=', ', end='.')
print(' Sum: ', end='')
print(sum(primary_diagonal))
print('Secondary diagonal: ', end='')
print(*secondary_diagonal, sep=', ', end='.')
print(' Sum: ', end='')
print(sum(secondary_diagonal))
