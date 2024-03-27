from collections import deque

food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    order = orders.popleft()
    if food >= order:
        orders.popleft()
        food -= order
    else:
        print(f'Orders left: ', *orders)
        break
else:
    print('Orders complete')
