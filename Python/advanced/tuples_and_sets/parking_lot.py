n = int(input())

parking_lot = set()

for _ in range(n):
    command, number = input().split(', ')
    if command == 'IN':
        parking_lot.add(number)
    elif command == 'OUT':
        parking_lot.remove(number)

if parking_lot:
    for number in parking_lot:
        print(number)
else:
    print("Parking Lot is Empty")
