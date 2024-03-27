class sequence_repeat:

    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.count = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.number:
            self.number -= 1
            self.count += 1
            if self.count == len(self.sequence):
                self.count = 0
            return self.sequence[self.count]

        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')