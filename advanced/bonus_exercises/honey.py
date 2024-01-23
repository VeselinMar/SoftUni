from collections import deque

bees = deque(int(bee) for bee in input().split())
nectar_deque = deque(int(nectar) for nectar in input().split())
symbols = deque(symbol for symbol in input().split())

total_honey_made = 0

functions = {
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else 0,
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b
}
while bees and nectar_deque:
    curr_bee = bees.popleft()
    curr_nectar = nectar_deque.pop()

    if curr_nectar < curr_bee:
        bees.appendleft(curr_bee)
    else:
        total_honey_made += abs(functions[symbols.popleft()](curr_bee, curr_nectar))
print(f"Total honey made: {abs(total_honey_made)}")

if bees:
    print('Bees left: ', end='')
    print(*bees, sep=', ')
if nectar_deque:
    print('Nectar left: ', end='')
    print(*nectar_deque, sep=', ')
