from collections import deque

line = deque(input().split())

numbers = deque()
for symbol in line:
    if not symbol.isdigit() and len(symbol) == 1:
        if symbol == '*':
            while len(numbers) > 1:
                number_1 = int(numbers.popleft())
                number_2 = int(numbers.popleft())
                numbers.appendleft(number_1 * number_2)
        elif symbol == '+':
            while len(numbers) > 1:
                number_1 = int(numbers.popleft())
                number_2 = int(numbers.popleft())
                numbers.appendleft(number_1 + number_2)
        elif symbol == '-':
            while len(numbers) > 1:
                number_1 = int(numbers.popleft())
                number_2 = int(numbers.popleft())
                numbers.appendleft(number_1 - number_2)
        elif symbol == '/':
            while len(numbers) > 1:
                number_1 = int(numbers.popleft())
                number_2 = int(numbers.popleft())
                numbers.appendleft(number_1 // number_2)
    else:
        numbers.append(int(symbol))

print(*numbers)
