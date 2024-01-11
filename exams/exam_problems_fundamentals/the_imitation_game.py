def move(text: str, count_symbols: int):
    new_message = text[0:count_symbols]
    text = text[count_symbols:] + new_message
    return text


def insert(text: str, index: int, value: str):
    part_1 = text[:index] + value
    part_2 = text[index:]
    return part_1 + part_2


def change_all(text: str, substring: str, replacement: str):
    return text.replace(substring, replacement)


message = input()

command = input()
while command != "Decode":
    mod_command = command.split("|")
    action = mod_command[0]
    if action == "Move":
        message = move(message, int(mod_command[1]))
    elif action == "Insert":
        message = insert(message, int(mod_command[1]), mod_command[2])
    elif action == "ChangeAll":
        message = change_all(message, mod_command[1], mod_command[2])
    command = input()

print(f"The decrypted message is: {message}")
