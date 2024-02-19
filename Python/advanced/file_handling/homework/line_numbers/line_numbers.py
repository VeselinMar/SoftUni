punctuation_marks = (",", ".", "-", "'", "!", "?", ":", ";", "(", ")", "[", "]", "{", "}", "_")

try:
    with open('text.txt', 'r') as line_numbers_file:
        text = line_numbers_file.readlines()

except FileNotFoundError:
    pass

f = open('output.txt', 'w+')

try:
    text_line = 0
    for line in text:
        line = line.strip("\n")
        text_line += 1
        letters, punctuation = 0, 0
        for symbol in line:
            if symbol.isalpha():
                letters += 1
            elif symbol in punctuation_marks:
                punctuation += 1

        f.write(f'Line: {text_line} {line} ({letters})({punctuation}) \n')

except FileNotFoundError:
    pass

f.close()
