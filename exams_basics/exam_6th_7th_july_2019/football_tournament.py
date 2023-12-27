import sys

name_team = input()
games_played = int(input())

if games_played == 0:
    print(f"{name_team} hasn't played any games during this season.")
    sys.exit()

wins = 0
draws = 0
loses = 0
points = 0

for games in range(games_played):
    game_score = input()

    if game_score == 'W':
        wins += 1
        points += 3
    elif game_score == 'D':
        draws += 1
        points += 1
    elif game_score == 'L':
        loses += 1

print(f'{name_team} has won {points} points during this season.')
print('Total stats:')
print(f'## W: {wins}')
print(f'## D: {draws}')
print(f'## L: {loses}')
print(f'Win rate: {wins / games_played * 100:.2f}%')
