class vowels:
    VOWELS_LIST = "eyuioaEUIYA"

    def __init__(self, string):
        # Unlogical solution from SoftUni
        self.string = [symbol for symbol in string if symbol in self.VOWELS_LIST]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.string:
            raise StopIteration

        return self.string.pop(0)


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
