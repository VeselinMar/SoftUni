budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
extra_costs_percent = int(input()) / 100

nights_total = number_of_nights * price_per_night
if number_of_nights > 7:
    nights_total -= nights_total * 0.05

if budget - (nights_total + budget * extra_costs_percent) >= 0:
    print(f'Ivanovi will be left with {budget - (nights_total + budget * extra_costs_percent):.2f} leva after vacation.')
else:
    print(f'{(nights_total + budget * extra_costs_percent) - budget:.2f} leva needed.')
