# import deque from collections
from collections import deque
# initiate a queue with elements
kids = input().split()
kids_in_circle = deque()
for kid in range(len(kids)):
    kids_in_circle.append(kids[kid])
# for n rotations first element goes to the back of the queue. First element gets popped.
n = int(input())
while len(kids_in_circle) > 1:
    for _ in range(n - 1):
        kids_in_circle.rotate(-1)
    print(f'Removed {kids_in_circle.popleft()}')
# print the remaining element
print(f'Last is {kids_in_circle.pop()}')
