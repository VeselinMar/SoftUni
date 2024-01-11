film_budget = float(input())
extras = int(input())
price_costume_per_extra = float(input())

decor = film_budget * 0.1

if extras > 150:
    price_costume_per_extra *= 0.9

costs = extras * price_costume_per_extra + decor

if costs > film_budget:
    print('Not enough money!')
    print(f'Wingard needs {costs - film_budget:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {film_budget - costs:.2f} leva left.')