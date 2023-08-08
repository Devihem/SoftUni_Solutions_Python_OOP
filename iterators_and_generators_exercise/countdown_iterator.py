class countdown_iterator:
    def __init__(self, period):
        self.period = period + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.period == 0:
            raise StopIteration
        self.period -= 1
        return self.period


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
