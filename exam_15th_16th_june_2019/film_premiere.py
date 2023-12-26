film = input()
package = input()
number_of_tickets = int(input())

price_per_ticket = 0
if film == 'John Wick':
    if package == 'Drink':
        price_per_ticket = 12
    elif package == 'Popcorn':
        price_per_ticket = 15
    elif package == 'Menu':
        price_per_ticket = 19
elif film == 'Star Wars':
    if package == 'Drink':
        price_per_ticket = 18
    elif package == 'Popcorn':
        price_per_ticket = 25
    elif package == 'Menu':
        price_per_ticket = 30
elif film == 'Jumanji':
    if package == 'Drink':
        price_per_ticket = 9
    elif package == 'Popcorn':
        price_per_ticket = 11
    elif package == 'Menu':
        price_per_ticket = 14

total_price = number_of_tickets * price_per_ticket

if film == 'Star Wars' and number_of_tickets >= 4:
    total_price -= total_price * 0.3
if film == 'Jumanji' and number_of_tickets == 2:
    total_price -= total_price * 0.15

print(f"Your bill is {total_price:.2f} leva.")
