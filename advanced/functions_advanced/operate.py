def operate(*args):

    def addition():
        result = 0
        for symbol in args:
            if isinstance(symbol, int):
                result += symbol
        return result

    def subtraction():
        result = args[1]
        for symbol in args[2:]:
            if isinstance(symbol, int):
                result -= symbol
        return result

    def multiplication():
        result = args[1]
        for symbol in args[2:]:
            if isinstance(symbol, int):
                result *= symbol
        return result

    def division():
        result = args[1]
        for symbol in args[2:]:
            if isinstance(symbol, int) and symbol != 0:
                result /= symbol
        return result

    if '+' in args:
        return addition()
    elif '-' in args:
        return subtraction()
    elif '*' in args:
        return multiplication()
    elif '/' in args:
        return division()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 20, 2, 2))