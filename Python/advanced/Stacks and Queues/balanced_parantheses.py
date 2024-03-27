def is_balanced(parentheses: str):
    if len(parentheses) % 2 != 0:
        return False
    forbidden = ['(]', '(}', '[)', '[}', '{)', '{]']
    for item in forbidden:
        if item in parentheses:
            return False
    else:
        return True


line = input()
if is_balanced(line):
    print('YES')
else:
    print('NO')
