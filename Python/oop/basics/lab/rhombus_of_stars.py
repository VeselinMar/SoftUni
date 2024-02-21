N = int(input())


def print_rhombus(num):

    def rhombus_top():
        for row in range(1, num + 1):
            print(" " * (num - row), end='')
            print("* " * row)

    def rhombus_bottom():
        for row in range(num - 1, 0, -1):
            print(' ' * (num - row), end='')
            print('* ' * row)

    rhombus_top()
    rhombus_bottom()


print_rhombus(N)
