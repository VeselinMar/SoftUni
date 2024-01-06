def add_substring(line: str, sub: str):
    return line + sub


def upgrade_char(line: str, char: str):
    new = ''
    for c in line:
        if c == char:
            new += chr(ord(c)+1)
        else:
            new += c
    return new


def index_char(line: str, char: str):
    indexes = [str(index) for index, c in enumerate(line) if c == char]
    if indexes:
        return ' '.join(indexes)
    else:
        return 'None'


def remove_substring(line: str, sub: str):
    return line.replace(sub, '')


empty_not_for_long = ''

command = input()
while command != 'End':
    if command == 'Print':
        print(empty_not_for_long)
    else:
        command = command.split()
        if command[0] == 'Add':
            substring = command[1]
            empty_not_for_long = add_substring(empty_not_for_long, substring)
        elif command[0] == 'Upgrade':
            character = command[1]
            empty_not_for_long = upgrade_char(empty_not_for_long, character)
        elif command[0] == 'Index':
            character = command[1]
            print(index_char(empty_not_for_long, character))
        elif command[0] == 'Remove':
            substring = command[1]
            empty_not_for_long = remove_substring(empty_not_for_long, substring)
    command = input()
