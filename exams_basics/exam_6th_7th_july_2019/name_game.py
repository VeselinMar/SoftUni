points = 0
player_name = ''
winning_player = ''
winning_score = 0
while True:
    player_name = input()
    if player_name == 'Stop':
        break
    for letter in player_name:
        guess = int(input())
        if ord(letter) == guess:
            points += 10
        else:
            points += 2
    if points >= winning_score:
        winning_player = player_name
        winning_score = points

    points = 0

print(f"The winner is {winning_player} with {winning_score} points!")
