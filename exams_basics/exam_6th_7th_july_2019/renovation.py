import math

wall_height = int(input())
wall_width = int(input())
percent_not_to_paint = int(input()) / 100

litres_of_paint = 0
walls = wall_width * wall_height * 4
to_paint = math.ceil(walls - percent_not_to_paint * walls)

while to_paint >= 0:
    litres_of_paint = input()
    if litres_of_paint == 'Tired!':
        print(f'{to_paint} quadratic m left.')
        break

    litres_of_paint = int(litres_of_paint)
    to_paint -= litres_of_paint
    if to_paint == 0:
        print(f'All walls are painted! Great job, Pesho!')
        break

if to_paint < 0:
    print(f'All walls are painted and you have {abs(to_paint)} l paint left!')
