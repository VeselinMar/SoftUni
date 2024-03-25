def vowel_filter(function):

    def wrapper():
        res = function()
        vowels = ["a", "e", "i", "u", "o", "y"]
        return [letter for letter in res if letter in vowels]
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
