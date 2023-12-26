saloon_capacity = int(input())
capacity_remaining = saloon_capacity
profit = 0
while capacity_remaining >= 0:
    line = input()
    if line == 'Movie time!':
        print(f'There are {capacity_remaining} seats left in the cinema.')
        break
    if not capacity_remaining or int(line) > capacity_remaining:
        print('The cinema is full.')
        break
    bill = 0
    capacity_remaining -= int(line)
    price_reduction_check = int(line) / 3
    if price_reduction_check == int(price_reduction_check):
        bill -= 5
    bill += int(line) * 5
    profit += bill

print(f'Cinema income - {profit} lv.')
