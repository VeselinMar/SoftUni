film_budget = float(input())
destination = input()
season = input()
number_of_days = int(input())

price = 0
if season == 'Winter':
    if destination == 'Dubai':
        price = 45000
    elif destination == 'Sofia':
        price = 17000
    elif destination == 'London':
        price = 24000
elif season == 'Summer':
    if destination == 'Dubai':
        price = 40000
    elif destination == 'Sofia':
        price = 12500
    elif destination == 'London':
        price = 20250

if destination == 'Dubai':
    price -= price * 0.3
if destination == 'Sofia':
    price += price * 0.25

price = price * number_of_days

if film_budget >= price:
    print(f"The budget for the movie is enough! We have {film_budget - price:.2f} leva left!")
else:
    print(f"The director needs {price - film_budget:.2f} leva more!")
