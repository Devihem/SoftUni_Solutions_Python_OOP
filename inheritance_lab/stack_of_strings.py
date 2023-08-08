class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return True if len(self.data) == 0 else False

    def __str__(self):
        return f"[{', '.join([x for x in self.data[::-1]])}]"
