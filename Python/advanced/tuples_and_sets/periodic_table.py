n = int(input())

table = set()

for _ in range(n):
    elements = input().split()
    for element in elements:
        table.add(element)

for element in table:
    print(element)
