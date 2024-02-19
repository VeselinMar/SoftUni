orders = {}
line = input()
while line != 'buy':
    line = line.split(' ')
    name, price, quantity = line[0], float(line[1]), int(line[2])
    if name not in orders:
        orders[name] = {'price': price, 'quantity': quantity}
    else:
        orders[name]['price'] = price
        orders[name]['quantity'] += quantity
    line = input()

for name, details in orders.items():
    total = details['price'] * details['quantity']
    print(f'{name} -> {total:.2f}')
