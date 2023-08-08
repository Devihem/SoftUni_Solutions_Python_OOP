class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []  # obj
        self.movies_owned = []  # obj

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value == "":
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        result = [f"Username: {self.username}, Age: {self.age}", "Liked movies:"]

        liked_movies_result = [movie.details() for movie in self.movies_liked]
        if not liked_movies_result:
            liked_movies_result = ["No movies liked."]

        result.extend(liked_movies_result)

        result.append("Owned movies:")

        owned_movies_result = [movie.details() for movie in self.movies_owned]
        if not owned_movies_result:
            owned_movies_result = ["No movies owned."]

        result.extend(owned_movies_result)

        return '\n'.join(result)
