beverage = input()
sugar_init = input()
beverages_total = int(input())

price_per_beverage = 0

if beverage == 'Espresso':
    price_per_beverage = 1
    if sugar_init == 'Without':
        price_per_beverage = 0.90
    if sugar_init == 'Extra':
        price_per_beverage = 1.20
    if beverages_total >= 5:
        price_per_beverage -= price_per_beverage * 0.25
if beverage == 'Cappuccino':
    price_per_beverage = 1.20
    if sugar_init == 'Without':
        price_per_beverage = 1
    if sugar_init == 'Extra':
        price_per_beverage = 1.60
if beverage == 'Tea':
    price_per_beverage = 0.60
    if sugar_init == 'Without':
        price_per_beverage = 0.50
    if sugar_init == 'Extra':
        price_per_beverage = 0.70

if sugar_init == 'Without':
    price_per_beverage -= price_per_beverage * 0.35

sum_total = price_per_beverage * beverages_total
if sum_total > 15:
    sum_total -= sum_total * 0.2

print(f'You bought {beverages_total} cups of {beverage} for {sum_total:.2f} lv.')
