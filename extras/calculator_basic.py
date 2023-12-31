def addition(num_1: float, num_2: float):
    return num_1 + num_2


def subtraction(num_1: float, num_2: float):
    return num_1 - num_2


def multiplication(num_1: float, num_2: float):
    return num_1 * num_2


def division(num_1: float, num_2: float):
    if num_2 == 0:
        return "You can not divide by zero!"
    return num_1 / num_2


result = 0
operation = input().split()
while operation != 'quit':
    a = float(operation[0])
    b = float(operation[2])
    symbol = operation[1]
    if symbol == '+':
        result = addition(a, b)
        print(result)
    if symbol == '-':
        result = subtraction(a, b)
        print(result)
    if symbol == '*':
        result = multiplication(a, b)
        print(result)
    if symbol == '/':
        result = division(a, b)
        print(result)
    operation = input().split()
