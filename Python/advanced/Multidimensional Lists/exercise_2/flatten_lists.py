line = [sub for sub in input().split('|')]

matrix = []
for sub in reversed(line):
    matrix.extend(sub.split())

print(*matrix)
