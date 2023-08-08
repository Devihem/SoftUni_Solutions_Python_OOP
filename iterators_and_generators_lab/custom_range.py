class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.counter = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter > self.end:
            raise StopIteration
        result = self.counter
        self.counter += 1
        return result


one_to_ten = custom_range(0, 10)
for num in one_to_ten:
    print(num)
