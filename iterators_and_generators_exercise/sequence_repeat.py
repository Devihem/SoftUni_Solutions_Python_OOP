class sequence_repeat:
    def __init__(self, string, len_int):
        self.string = string
        self.len_int = len_int
        self.current_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.len_int == 0:
            raise StopIteration
        self.len_int -= 1
        self.current_index += 1

        if self.current_index > len(self.string) - 1:
            self.current_index = 0

        return self.string[self.current_index]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
