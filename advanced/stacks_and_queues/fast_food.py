# import deque from collections
from collections import deque
# quantity of food for the day
quantity_of_food = int(input())
# save orders into a queue and make a second queue from which to take the biggest order
orders = input().split()
orders_queue = deque()
biggest_order = deque()
for order in orders:
    orders_queue.append(int(order))
    if biggest_order:
        if int(order) > biggest_order[-1]:
            biggest_order.append(int(order))
        else:
            biggest_order.appendleft(int(order))
    else:
        biggest_order.append(int(order))
# print biggest order
print(biggest_order[-1])
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
