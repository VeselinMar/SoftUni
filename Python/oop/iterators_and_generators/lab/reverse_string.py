def reverse_text(string: str):
    last_element = len(string) - 1
    while last_element >= 0:
        yield string[last_element]
        last_element -= 1


for char in reverse_text("step"):
    print(char, end='')