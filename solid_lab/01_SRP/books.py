class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None


book1 = Book('Book_name_1', 'Author _ of Book_1')
book1.turn_page(50)

book2 = Book('Book_name_2', 'Author _ of Book_2')
book2.turn_page(150)

library = Library()
library.add_book(book1)
library.add_book(book2)

searched_book = library.find_book("Book_name_2")
print(searched_book.title)