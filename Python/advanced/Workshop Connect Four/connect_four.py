class FullColumnError(Exception):
    pass


class InvalidColumnChoice(Exception):
    pass


ROWS = 6
COLS = 7
MAXIMUM_CONNECTIONS = 4


DIRECTION_MAPPER = {
    "left": (0, -1),
    "up": (-1, 0),
    "main_diagonal": (-1, -1),
    "other_diagonal": (-1, 1),

}


def travel_direction(coordinates, current_row, current_col, game_board, element):

    count = 0
    row_direction, col_direction = coordinates

    for i in range(1, MAXIMUM_CONNECTIONS):
        next_element_row_index = current_row + row_direction * i
        next_element_col_index = current_col + col_direction * i

        try:
            if board[next_element_row_index][next_element_col_index] == element:
                count += 1
            else:
                return count

        except IndexError:
            return count


def travel_opposite_direction(coordinates, current_row, current_col, game_board, element):
    count = 0
    row_direction, col_direction = coordinates

    for i in range(1, MAXIMUM_CONNECTIONS):
        next_element_row_index = current_row - row_direction * i
        next_element_col_index = current_col - col_direction * i

        try:
            if board[next_element_row_index][next_element_col_index] == element:
                count += 1
            else:
                return count

        except IndexError:
            return count


def is_winner(current_row_index, current_col_index, game_board):
    for direction, coords in DIRECTION_MAPPER.items():
        searched_element = board[current_row_index][current_col_index]
        travel_direction_count = (travel_direction
                                  (coords, current_row_index, current_col_index, game_board, searched_element))
        travel_opposite_direction_count = (travel_opposite_direction
                                           (coords, current_row_index, current_col_index, game_board, searched_element))

        if travel_direction_count + travel_opposite_direction_count + 1 >= MAXIMUM_CONNECTIONS:
            return True

    else:
        return False


def print_board(game_board):
    for row in board:
        print(row)


def validate_column_choice(col):
    if 1 <= col <= COLS:
        return True
    else:
        raise InvalidColumnChoice


def get_first_available_row(col_index, game_board):

    for row_index in range(ROWS-1, - 1, -1):
        if game_board[row_index][col_index] == 0:
            return row_index

    else:
        raise FullColumnError("This column is full, please select another one.")


def is_board_full(turns):
    return ROWS*COLS > turns


board = []

for _ in range(ROWS):
    board.append([0 for _ in range(COLS)])

turns = 1

while True:
    player = 2 if turns % 2 == 0 else 1

    try:
        column = int(input(f'Player {player}, please choose a column: '))
        validate_column_choice(column)
        column_index = int(column) - 1
        row = get_first_available_row(column_index, board)
        board[row][column_index] = player
        if is_winner(row, column_index, board):
            break
        if is_board_full(turns):
            print('Board is full, nobody wins.')
            exit(0)
    except FullColumnError:
        print('This column is already full, select another one')
        continue
    except (InvalidColumnChoice, ValueError):
        print(f'This column is invalid, please select a number between 1 and {COLS}')
        continue

    print_board(board)
    turns += 1

print_board(board)
print(f"Winner is player {player}")
