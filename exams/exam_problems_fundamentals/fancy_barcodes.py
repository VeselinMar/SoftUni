import re

n = int(input())

pattern = r"@[#]+([A-Z]([a-zA-Z0-9]+){4,}[A-Z])@[#]+"

for _ in range(n):
    line = input()
    match = re.search(pattern, line)
    if match is None:
        print("Invalid barcode")
    else:
        group = ''
        for symbol in match.group(1):
            if symbol.isdigit():
                group += symbol
        if group:
            print(f"Product group: {group}")
        else:
            print("Product group: 00")
