from user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}  # {author:[ author_books ] }
        self.rented_books = {}  # ({usernames: {book names: days to return}})

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if book_name in self.books_available[author]:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)

            if user.username in self.rented_books:
                self.rented_books[user.username][book_name] = days_to_return
            else:
                self.rented_books[user.username] = {book_name: days_to_return}

            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for user_rented_books in self.rented_books.values():
            if book_name in user_rented_books.keys():
                return f'The book "{book_name}" is already rented ' \
                       f'and will be available in {user_rented_books[book_name]} days!'

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            self.books_available[author].append(book_name)
            del self.rented_books[user.username][book_name]
            user.books.remove(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"
