class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.counter_loop = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter_loop + 1 >= self.count:
            raise StopIteration
        self.counter_loop += 1
        return self.step * self.counter_loop


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
