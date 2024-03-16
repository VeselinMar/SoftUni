class vowels:

    def __init__(self, string):
        self.string = string
        self.count = 0
        _vowels_list = ['a', 'o', 'u', 'y', 'e', 'i']
        self.vowels_collection = [letter for letter in self.string if letter.lower() in _vowels_list]
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.count < len(self.vowels_collection):
            vowel = self.vowels_collection[self.count]
            self.count += 1
            return vowel
        else:
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
