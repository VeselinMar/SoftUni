symbols_to_replace = ("-", ",", ".", "!", "?")

try:
    with open('text.txt', 'r') as even_lines_file:
        text = even_lines_file.readlines()

except FileNotFoundError:
    pass

for row in range(0, len(text), 2):

    for symbol in symbols_to_replace:
        text[row] = text[row].replace(symbol, "@")

    print(*text[row].split()[::-1])
