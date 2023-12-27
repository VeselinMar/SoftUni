sold_games = int(input())

hearthstone = 0
fornite = 0
overwatch = 0
others = 0

for games in range(sold_games):
    game = input()
    if game == 'Hearthstone':
        hearthstone += 1
    elif game == 'Fornite':
        fornite += 1
    elif game == 'Overwatch':
        overwatch += 1
    else:
        others += 1

print(f'Hearthstone - {(hearthstone / sold_games) * 100:.2f}%')
print(f'Fornite - {(fornite / sold_games) * 100:.2f}%')
print(f'Overwatch - {(overwatch / sold_games) * 100:.2f}%')
print(f'Others - {(others / sold_games) * 100:.2f}%')
