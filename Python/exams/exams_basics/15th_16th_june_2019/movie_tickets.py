a1 = int(input())
a2 = int(input())
n = int(input())

symbol_1 = ''
symbol_2 = 0
symbol_3 = 0
symbol_4 = 0

for symbol in range(a1, a2):
    symbol_1 = chr(symbol)
    for symbols in range(1, n):
        symbol_2 = symbols
        for sym in range(1, n // 2):
            symbol_3 = sym

            symbol_4 = ord(symbol_1)

            sum_s234 = symbol_2 + symbol_3 + symbol_4
            if symbol_4 % 2 != 0 and sum_s234 % 2 != 0:
                print(f"{symbol_1}-{symbol_2}{symbol_3}{symbol_4}")
