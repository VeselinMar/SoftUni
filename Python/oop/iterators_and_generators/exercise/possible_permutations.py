def possible_permutations(list_input: list):
    def dfs(elements, path):
        if not elements:
            yield path
        for i, element in enumerate(elements):
            if element not in path:
                yield from dfs(elements[:i] + elements[i + 1:], path + [element])

    for permutation in dfs(list_input, []):
        yield permutation


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]
