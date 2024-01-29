def rectangle(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        return 'Enter valid values!'

    def area():
        return a * b

    def perimeter():
        return 2*(a+b)

    return f'Rectangle area: {area()}\nRectangle perimeter: {perimeter()}'


print(rectangle(2, 10))
print(rectangle('2', 10))
