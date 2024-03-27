def recursive_power(number: int, power: int):
    result = 1

    def power_up():
        return result * number

    for _ in range(power):
        result = power_up()

    return result


print(recursive_power(2, 10))
print(recursive_power(10, 100))
