class Book:
    def __init__(self, name, author, page):
        self.name = name
        self.author = author
        self.page = page


book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.page)
