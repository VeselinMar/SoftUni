budget = float(input())
number_of_series = int(input())

cost = 0
for series in range(number_of_series):
    name_of_series = input()
    price_for_series = float(input())
    if name_of_series == 'Thrones':
        cost += price_for_series * 0.5
    elif name_of_series == 'Lucifer':
        cost += price_for_series * 0.6
    elif name_of_series == 'Protector':
        cost += price_for_series * 0.7
    elif name_of_series == 'TotalDrama':
        cost += price_for_series * 0.8
    elif name_of_series == 'Area':
        cost += price_for_series * 0.9
    else:
        cost += price_for_series

if budget >= cost:
    print(f"You bought all the series and left with {budget - cost:.2f} lv.")
else:
    print(f"You need {cost - budget:.2f} lv. more to buy the series!")
