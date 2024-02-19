def make_upper(email: str):
    global test
    test = email.upper()
    return test


def make_lower(email: str):
    global test
    test = email.lower()
    return test


def get_domain(email: str, count: int):
    return email[-count::]


def get_username(email: str):
    if '@' not in email:
        return f"The email {email} doesn't contain the @ symbol."
    email_split = test.split('@')
    return email_split[0]


def replace(email: str, given: str):
    global test
    result = ''
    for char in email:
        if char == given:
            result += '-'
        else:
            result += char
    test = result
    return result


def encrypt(email: str):
    result = ''
    count = 0
    for char in email:
        result += str(ord(char))
        if count != len(email):
            result += ' '
    return result


test = input()

command = input()
while command != 'Complete':
    if command == 'Make Upper':
        print(make_upper(test))
    elif command == 'Make Lower':
        print(make_lower(test))
    elif 'GetDomain' in command:
        command, count_of_chars = command.split()
        print(get_domain(test, int(count_of_chars)))
    elif command == 'GetUsername':
        print(get_username(test))
    elif 'Replace' in command:
        command, character = command.split()
        print(replace(test, character))
    elif command == 'Encrypt':
        print(encrypt(test))
    command = input()
