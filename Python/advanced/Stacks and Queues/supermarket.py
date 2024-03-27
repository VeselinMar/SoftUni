# import deque to use a queue
from collections import deque

# initiate a queue
queue = deque()
line = input()
while line != 'End':
    if line == 'Paid':
        # use the method popleft to take the leftmost element
        while queue:
            print(queue.popleft())
    else:
        queue.append(line)
    line = input()
# print out the remaining number of people
print(f'{len(queue)} people remaining.')
