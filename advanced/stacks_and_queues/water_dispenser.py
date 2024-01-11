# import deque from collections
from collections import deque
# initiate a variable to keep the water quantity in
water_quantity = int(input())
# initiate a queue
waiting_line = deque()
command = input()
while command != 'Start':
    waiting_line.append(command)
    command = input()
# initiate second loop to manipulate the waiting line
command = input()
while command != 'End':
    if 'refill' in command:
        command = command.split()
        _, litres = command[0], int(command[1])
        water_quantity += litres
    else:
        litres_needed = int(command)
        if litres_needed <= water_quantity:
            print(f'{waiting_line.popleft()} got water')
            water_quantity -= litres_needed
        else:
            print(f'{waiting_line.popleft()} must wait')
    command = input()
# print out the remaining water quantity
print(f'{water_quantity} liters left')
