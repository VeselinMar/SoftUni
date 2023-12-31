def linear_search(input_list: list, target: str):
    for index, item in enumerate(input_list):
        if item == target:
            return index
    return -1


list_enter = input().split()
searched = input()

result = linear_search(list_enter, searched)
if result != -1:
    print(f'The target element {searched} is at index {result}.')
else:
    print(f"The target element {searched} was not found in the list.")
