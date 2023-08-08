from library import Library
from user import User


class Registration:

    def add_user(self, user: User, library: Library):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"

        library.user_records.append(user)

    def remove_user(self, user: User, library: Library):

        if user in library.user_records:
            library.user_records.remove(user)

        return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        for user_id_search in library.user_records:
            if user_id_search.user_id == user_id:
                if user_id_search.username != new_username:

                    if user_id_search.username in library.rented_books.keys():
                        books_rental_copy = library.rented_books[user_id_search.username]
                        del library.rented_books[user_id_search.username]
                        # mom spaghetti
                        library.rented_books[new_username] = books_rental_copy
                    user_id_search.username = new_username
                    return f"Username successfully changed to: {new_username} for user id: {user_id}"

                else:
                    return "Please check again the provided username -" \
                           " it should be different than the username used so far!"
            else:
                return f"There is no user with id = {user_id}!"
