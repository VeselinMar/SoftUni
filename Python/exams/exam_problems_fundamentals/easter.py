line = input()
command = input()
while command != 'Easter':
    command = command.split()
    task = command[0]
    if task == 'Replace':
        current_char, new_char = command[1], command[2]
        if current_char not in line:
            print(line)
        else:
            new_line = ''
            for char in line:
                if char == current_char:
                    new_line += new_char
                else:
                    new_line += char
            line = new_line
            print(line)
    elif task == 'Remove':
        substring = command[1]
        if substring not in line:
            print(line)
        else:
            line = line.replace(substring, '')
            print(line)
    elif task == 'Includes':
        substring = command[1]
        if substring in line:
            print('True')
        else:
            print('False')
    elif task == 'Change':
        capitalization = command[1]
        if capitalization == 'Lower':
            line = line.lower()
            print(line)
        elif capitalization == 'Upper':
            line = line.upper()
            print(line)
    elif task == 'Reverse':
        start_index, end_index = command[1], command[2]
        if int(end_index) < len(line):
            print(''.join(reversed(line[int(start_index):int(end_index)+1])))
    command = input()
