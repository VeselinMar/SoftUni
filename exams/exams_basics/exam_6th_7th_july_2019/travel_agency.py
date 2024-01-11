import sys

town_name = input()
packet = input()
vip = input()
days = int(input())
town_packet_check = True
price = 0
if town_name != 'Bansko' and town_name != 'Borovets' and town_name != 'Varna' and town_name != 'Burgas':
    town_packet_check = False
if packet != 'noEquipment' and packet != 'withEquipment' and packet != 'noBreakfast' and packet != 'withBreakfast':
    town_packet_check = False

if not town_packet_check:
    print('Invalid input!')
    sys.exit()
if days < 1:
    print("Days must be positive number!")
    sys.exit()

if town_name == 'Bansko' or town_name == 'Borovets':
    if packet == 'withEquipment':
        price = 100
        if vip == 'yes':
            price -= price * 0.1
    elif packet == 'noEquipment':
        price = 80
        if vip == 'yes':
            price -= price * 0.05
if town_name == 'Varna' or town_name == 'Burgas':
    if packet == 'withBreakfast':
        price = 130
        if vip == 'yes':
            price -= price * 0.12
    elif packet == 'noBreakfast':
        price = 100
        if vip == 'yes':
            price -= price * 0.07

if days > 7:
    days -= 1
total_price = price * days

print(f'The price is {total_price:.2f}lv! Have a nice time!')
