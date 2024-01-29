def even_odd_filter(**kwargs):
    result = {}

    def odd_filter():
        if 'odd' in kwargs.keys():
            key, value = 'odd', [int(num) for num in kwargs.get('odd') if num % 2 != 0]
            result[key] = value

    def even_filter():
        if 'even' in kwargs.keys():
            key, value = 'even', [int(num) for num in kwargs.get('even') if num % 2 == 0]
            result[key] = value

    odd_filter()
    even_filter()
    sorted_result = dict(sorted(result.items(), key=lambda item: -len(item[1])))
    return sorted_result


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
