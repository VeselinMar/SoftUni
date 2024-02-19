def age_assignment(*args, **kwargs):
    result = []
    args_list = [name for name in args]
    while args_list:
        name = args_list.pop()
        line = f"{name} is {kwargs[name[0]]} years old."
        result.append(line)

    return '\n'.join(sorted(result))


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))