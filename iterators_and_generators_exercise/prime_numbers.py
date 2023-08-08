def get_primes(numbers_list):
    for numb in numbers_list:
        if numb <= 1:
            continue
        for n in range(2, numb):
            if numb % n == 0:
                break
        else:
            yield numb


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0, 13, 97, 18, 23])))
