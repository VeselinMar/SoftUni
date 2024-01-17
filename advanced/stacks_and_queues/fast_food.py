# import deque from collections
from collections import deque
# quantity of food for the day
quantity_of_food = int(input())
# save orders into a queue
orders = input().split()
orders_queue = deque()
biggest_order = 0
for order in orders:
    orders_queue.append(int(order))
    if biggest_order:
        if int(order) > biggest_order:
            biggest_order = int(order)
    else:
        biggest_order = int(order)
# print biggest order
print(biggest_order)
# complete orders if quantity is enough
while orders_queue:
    if quantity_of_food >= orders_queue[0]:
        quantity_of_food -= orders_queue[0]
        orders_queue.popleft()
        # print if there are no remaining orders
        if not orders_queue:
            print('Orders complete')
    # print remaining orders if quantity is not enough
    else:
        if orders_queue:
            print(f'Orders left: ', end='')
            while orders_queue:
                orders_left = orders_queue.popleft()
                print(orders_left, end=' ')
