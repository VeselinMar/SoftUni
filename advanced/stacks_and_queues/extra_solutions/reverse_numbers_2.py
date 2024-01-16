from collections import deque

numbers = deque(input().split())  # [1, 2, 3, 4, 5]

numbers.reverse()
print(*numbers)  # *(unpack)
