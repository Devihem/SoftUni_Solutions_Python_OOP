def number_increment(numbers):
    def increase():
        return [numb + 1 for numb in numbers]

    return increase()


print(number_increment([1, 2, 3]))
