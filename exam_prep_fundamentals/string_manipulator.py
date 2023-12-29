string = input()

command = input()
while command != 'End':
    if command == 'Lowercase':
        string = string.lower()
        print(string)

    else:
        command = command.split(' ')
        if command[0] == 'Translate':
            char = command[1]
            replacement = command[2]
            if char in string:
                string = string.replace(char, replacement)
            print(string)

        elif command[0] == 'Includes':
            substring = command[1]
            if substring in string:
                print('True')
            else:
                print('False')

        elif command[0] == 'Start':
            substring = command[1]
            if string[0:len(substring)] == substring:
                print('True')
            else:
                print('False')

        elif command[0] == 'FindIndex':
            char = command[1]
            last_occurrence = string.rfind(char)
            print(last_occurrence)

        elif command[0] == 'Remove':
            start_index = int(command[1])
            count = int(command[2])
            string_first_half = string[0:start_index]
            string_second_half = string[(start_index + count):]
            string = string_first_half + string_second_half
            print(string)
    command = input()
