voucher_value = int(input())

tickets = 0
others = 0
while voucher_value:
    price = 0
    product = input()
    if product == 'End':
        break

    elif len(product) > 8:
        price = ord(product[0]) + ord(product[1])
        if price <= voucher_value:
            tickets += 1
        else:
            break

    elif len(product) <= 8:
        price = ord(product[0])
        if price <= voucher_value:
            others += 1
        else:
            break

    voucher_value -= price

print(tickets)
print(others)
