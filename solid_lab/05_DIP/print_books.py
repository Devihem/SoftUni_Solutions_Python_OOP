class Book:
    def __init__(self, content: str):
        self.content = content


class NormalFormatter:
    @staticmethod
    def format(book: Book) -> str:
        return book.content


class SpecialFormatter:
    @staticmethod
    def format(book: Book) -> str:
        return f"-----------------------\n" \
               f"{book.content}\n" \
               f"-----------------------\n"


class Printer:
    @staticmethod
    def get_book(book: Book, formatter_version):
        formatter = formatter_version.format(book)
        print(formatter)


book_233 = Book('Some Content')
Printer.get_book(book_233, SpecialFormatter)
