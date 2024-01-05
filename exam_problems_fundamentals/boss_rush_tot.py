import re

n = int(input())
pattern = r'\|([A-Z]{4,})\|:\#([a-zA-Z]+ [a-zA-Z]+)#'

for _ in range(n):
    line = input()
    match = re.match(pattern, line)
    if match:
        print(f'{match.group(1)}, The {match.group(2)}'
              f'\n>> Strength: {len(match.group(1))} '
              f'\n>> Armor: {len(match.group(2))}')
    else:
        print('Access denied!')
