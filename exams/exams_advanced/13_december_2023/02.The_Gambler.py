n = int(input())

board = []
gambler_position = []

directions = {
    "left": (0, -1),
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
}

for row in range(n):
    line = [symbol for symbol in input()]
    board.append(line)
    for cell in line:
        if cell == "G":
            column = line.index("G")
            gambler_position = [row, line.index("G")]

total_amount = 100
jackpot = False

command = input()
while command != 'end':
    r, c = gambler_position
    row, col = directions.get(command)
    next_position = [r + row, c + col]
    if 0 > next_position[0] or next_position[0] >= n or 0 > next_position[1] or next_position[1] >= n:
        board[gambler_position[0]][gambler_position[1]] = "-"
        if total_amount > 0:
            total_amount = 0
        break

    elif board[next_position[0]][next_position[1]] == "W":
        board[gambler_position[0]][gambler_position[1]] = "-"
        total_amount += 100
        board[next_position[0]][next_position[1]] = "G"
        gambler_position = next_position[0], next_position[1]

    elif board[next_position[0]][next_position[1]] == "P":
        board[gambler_position[0]][gambler_position[1]] = "-"
        total_amount -= 200
        if total_amount <= 0:
            break
        board[next_position[0]][next_position[1]] = "G"
        gambler_position = next_position[0], next_position[1]

    elif board[next_position[0]][next_position[1]] == "J":
        jackpot = True
        board[gambler_position[0]][gambler_position[1]] = "-"
        total_amount += 100000
        board[next_position[0]][next_position[1]] = "G"
        gambler_position = next_position[0], next_position[1]
        break

    elif board[next_position[0]][next_position[1]] == "-":
        board[gambler_position[0]][gambler_position[1]] = "-"
        board[next_position[0]][next_position[1]] = "G"
        gambler_position = next_position[0], next_position[1]

    command = input()

if jackpot:
    print("You win the Jackpot!")

if total_amount <= 0:
    print("Game over! You lost everything!")

else:
    print(f"End of the game. Total amount: {total_amount}$")
    for line in board:
        print(''.join(line))
