def func_executor(*func_args):
    results = []
    for func, args in func_args:
        function_name = func.__name__
        function_result = func(*args)
        result_string = f'{function_name} - {function_result}'
        results.append(result_string)

    end_result = '\n'.join(results)
    return end_result


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result


def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result


print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))
