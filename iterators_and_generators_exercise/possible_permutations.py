from itertools import permutations


def possible_permutations(numbers):
    for combination in permutations(numbers, len(numbers)):
        yield list(combination)


[print(n) for n in possible_permutations([1, 2, 3])]
