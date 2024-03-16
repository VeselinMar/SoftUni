def genrange(start: int, end: int):
    i = start
    while i < end + 1:
        yield i
        i += 1


print(list(genrange(1, 10)))
