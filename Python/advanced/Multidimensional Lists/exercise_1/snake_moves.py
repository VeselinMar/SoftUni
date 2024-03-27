from collections import deque

r, c = [int(num) for num in input().split()]

snake = input()

overflow = []
matrix = []
for count in range(r):
    line = deque()

    if overflow:
        if count % 2 == 0:
            for char in overflow:
                line.append(char)
        else:
            for char in overflow:
                line.appendleft(char)
    while len(line) < c:
        if count > 0:
            if count % 2 != 0:
                for ind in range(len(snake)):
                    line.appendleft(snake[ind])

            else:
                for ind in range(len(snake)):
                    line.append(snake[ind])

        else:
            for ind in range(len(snake)):
                line.append(snake[ind])

    overflow = deque()
    while len(line) > c:
        if count % 2 == 0:
            remaining = line.pop()
            overflow.appendleft(remaining)
        else:
            remaining = line.popleft()
            overflow.appendleft(remaining)
    matrix.append(line)

for line in matrix:
    print(''.join(line))
