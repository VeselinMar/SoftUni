from collections import deque

def possible_permutations(list_input: list):
    def dfs(elements, path):
        if not elements:
            yield path
        seen = set()
        for i, element in enumerate(elements):
            if element not in seen:
                seen.add(element)
                yield from dfs(elements[:i] + elements[i + 1:], path + [element])

    list_input = list(list_input)  # Convert deque to list for slicing
    elements = len(list_input)
    for permutation in dfs(list_input, []):
        yield permutation


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]
