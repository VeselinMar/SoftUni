def concatenate(*args, **kwargs):
    concatenation_result = ''
    for arg in args:
        concatenation_result += arg

    def modify():
        if kwargs:
            modified_result = concatenation_result
            for key, value in kwargs.items():
                modified_result = modified_result.replace(key, value)
            return modified_result

        else:
            return concatenation_result

    return modify()


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
