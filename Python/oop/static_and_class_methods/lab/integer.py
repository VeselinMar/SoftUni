import math


class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(math.floor(float_value))

    @classmethod
    def from_roman(cls, value):
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        arabic = 0

        prev_value = 0
        for numeral in reversed(value):
            value = roman_numerals[numeral]
            if value < prev_value:
                arabic -= value
            else:
                arabic += value
            prev_value = value

        return cls(arabic)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"
        if '.' in value:
            return "wrong type"
        try:
            result = int(value)
            return cls(result)
        except ValueError:
            return "wrong type"


first_num = Integer(10)

print(first_num.value)

second_num = Integer.from_roman("IV")

print(second_num.value)

print(Integer.from_float("2.6"))

print(Integer.from_string(2.6))
