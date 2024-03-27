def even_odd(*args):
    if 'even' in args:
        return [int(num) for num in args if isinstance(num, int) and num % 2 == 0]
    else:
        return [int(num) for num in args if isinstance(num, int) and num % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
