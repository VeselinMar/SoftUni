class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.start = -self.step

    def __iter__(self):
        return self

    def __next__(self):
        if self.count:
            self.start += self.step
            self.count -= 1
            return self.start

        raise StopIteration


numbers = take_skip(10, 5)
for number in numbers:
    print(number)