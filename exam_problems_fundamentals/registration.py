def lower_upper(name: str, task: str):
    if task == 'Lower':
        new_name = name.lower()
        return new_name
    elif task == 'Upper':
        new_name = name.upper()
        return new_name


def reverse_from_to(name: str, start: int, end: int):
    part_of_name = name[start:end + 1]
    result = ''.join(reversed(part_of_name))
    return result


def substring(name: str, string: str):
    name = name.replace(string, '')
    return name


def replace_char(name: str, char: str):
    result = ''
    for symbol in name:
        if symbol != char:
            result += symbol
        else:
            result += '-'
    return result


def is_valid(name: str, char: str):
    if char in name:
        return f'Valid username.'
    else:
        return f'{char} must be contained in your username.'


line = input()

command = input()
while command != 'Registration':
    command = command.split()
    if command[0] == 'Letters':
        small_big = command[1]
        line = lower_upper(line, small_big)
        print(line)
    elif command[0] == 'Reverse':
        first, last = int(command[1]), int(command[2])
        if len(line) >= last >= 0 and first >= 0:
            print(reverse_from_to(line, first, last))
    elif command[0] == 'Substring':
        sub = command[1]
        if sub not in line:
            print(f"The username {line} doesn't contain {sub}.")
        else:
            print(substring(line, sub))
    elif command[0] == 'Replace':
        c = command[1]
        line = replace_char(line, c)
        print(line)
    elif command[0] == 'IsValid':
        print(is_valid(line, command[1]))

    command = input()
