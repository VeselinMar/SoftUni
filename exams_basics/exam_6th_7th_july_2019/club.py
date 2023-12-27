goal_win = float(input())
cocktail = input()
number_of_cocktails = int(input())

price_per_cocktail = 0
total_win = 0
while total_win < goal_win:
    for letters in cocktail:
        price_per_cocktail += 1
    cocktail_total = price_per_cocktail * number_of_cocktails
    if cocktail_total % 2 != 0:
        cocktail_total -= cocktail_total * 0.25
    total_win += cocktail_total

    if total_win >= goal_win:
        print('Target acquired.')
        break

    cocktail = input()
    if cocktail == 'Party!':
        print(f'We need {goal_win - total_win:.2f} leva more.')
        break

    number_of_cocktails = int(input())
    price_per_cocktail = 0


print(f'Club income - {total_win:.2f} leva.')
