import os
import fileinput
import sys


def create_file(name: str):
    f = open(name, 'w+')
    f.close()


def delete_file(name: str):
    os.remove(name)


def append_to_file(name: str, to_append: str):
    with open(name, 'a') as file:
        file.write(to_append + '\n')


def replace_in_file(name: str, old_str: str, new_str: str):
    for line in fileinput.input(name, inplace=1):
        if old_str in line:
            line = line.replace(old_str, new_str)
        sys.stdout.write(line)


command = input()
while command != 'End':
    command = command.split('-')
    file_name = command[1]

    if command[0] == 'Create':
        try:
            create_file(file_name)
        except FileExistsError:
            delete_file(file_name)
            create_file(file_name)

    elif command[0] == 'Add':
        content = command[2]
        try:
            append_to_file(file_name, content)
        except FileNotFoundError:
            create_file(file_name)
            append_to_file(file_name, content)

    elif command[0] == 'Replace':
        old, new = command[2], command[3]
        try:
            replace_in_file(file_name, old, new)
        except FileNotFoundError:
            print('An error occurred')

    elif command[0] == 'Delete':
        try:
            delete_file(file_name)
        except FileNotFoundError:
            print('An error occurred')

    command = input()
