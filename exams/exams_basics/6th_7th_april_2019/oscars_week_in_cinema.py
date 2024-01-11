film = input()
saloon_type = input()
tickets_bought = int(input())
price_per_ticket = 0

if saloon_type == 'normal':
    if film == 'A Star Is Born':
        price_per_ticket = 7.50
    elif film == 'Bohemian Rhapsody':
        price_per_ticket = 7.35
    elif film == 'Green Book':
        price_per_ticket = 8.15
    elif film == 'The Favourite':
        price_per_ticket = 8.75
elif saloon_type == 'luxury':
    if film == 'A Star Is Born':
        price_per_ticket = 10.50
    elif film == 'Bohemian Rhapsody':
        price_per_ticket = 9.45
    elif film == 'Green Book':
        price_per_ticket = 10.25
    elif film == 'The Favourite':
        price_per_ticket = 11.55
elif saloon_type == 'ultra luxury':
    if film == 'A Star Is Born':
        price_per_ticket = 13.50
    elif film == 'Bohemian Rhapsody':
        price_per_ticket = 12.75
    elif film == 'Green Book':
        price_per_ticket = 13.25
    elif film == 'The Favourite':
        price_per_ticket = 13.95

total_income = tickets_bought * price_per_ticket
print(f'{film} -> {total_income:.2f} lv.')
