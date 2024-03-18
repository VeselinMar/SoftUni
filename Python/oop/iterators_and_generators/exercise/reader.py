def read_next(*items):
    for item in items:
        if isinstance(item, dict):
            for key in item.keys():
                yield key
        for letter in item:
            yield letter


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
