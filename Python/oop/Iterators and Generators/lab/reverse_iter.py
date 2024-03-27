class reverse_iter:

    def __init__(self, iterable):
        self.iterable = iterable
        self.length = len(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        if self.length - 1 >= 0:
            self.length -= 1
            return self.iterable[self.length]
        raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
