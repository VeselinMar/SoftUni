def fibonacci():
    a = 0
    b = 1
    yield a
    yield b
    while True:
        a, b = b, b + a
        yield b


generator = fibonacci()
for i in range(10):
    print(next(generator))

generator = fibonacci()
for i in range(1):
    print(next(generator))
