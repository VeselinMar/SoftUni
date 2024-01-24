N = int(input())


primary_diagonal = []
secondary_diagonal = []
for count in range(N):
    row = [int(num) for num in input().split()]
    primary_diagonal.append(row[count])
    row.reverse()
    secondary_diagonal.append(row[count])

sum_primary = sum(primary_diagonal)
sum_secondary = sum(secondary_diagonal)
print(abs(sum_primary - sum_secondary))
