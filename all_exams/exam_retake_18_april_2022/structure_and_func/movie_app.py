from oop.all_exams.exam_retake_18_april_2022.structure_and_func.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []  # obj
        self.users_collection = []  # obj

    def register_user(self, username: str, age: int):
        if self.searching_user_by_username(username):
            raise Exception("User already exists!")

        created_user = User(username, age)
        self.users_collection.append(created_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie_obj):
        username_obj = self.searching_user_by_username(username)

        if not username_obj:
            raise Exception("This user does not exist!")

        if movie_obj in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        if movie_obj.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie_obj.title}!")

        self.movies_collection.append(movie_obj)
        username_obj.movies_owned.append(movie_obj)
        return f"{username} successfully added {movie_obj.title} movie."

    def edit_movie(self, username: str, movie_obj, **kwargs):
        username_obj = self.searching_user_by_username(username)

        if movie_obj not in self.movies_collection:
            raise Exception(f"The movie {movie_obj.title} is not uploaded!")

        if movie_obj.owner != username_obj:
            raise Exception(f"{username} is not the owner of the movie {movie_obj.title}!")

        for key, value in kwargs.items():
            setattr(movie_obj, key, value)

        return f"{username} successfully edited {movie_obj.title} movie."

    def delete_movie(self, username: str, movie_obj):

        username_obj = self.searching_user_by_username(username)

        if movie_obj not in self.movies_collection:
            raise Exception(f"The movie {movie_obj.title} is not uploaded!")

        if movie_obj.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie_obj.title}!")

        self.movies_collection.remove(movie_obj)
        username_obj.movies_owned.remove(movie_obj)
        return f"{username} successfully deleted {movie_obj.title} movie."

    def like_movie(self, username: str, movie_obj):

        username_obj = self.searching_user_by_username(username)

        if movie_obj.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie_obj.title}!")

        if movie_obj in username_obj.movies_liked:
            raise Exception(f"{username} already liked the movie {movie_obj.title}!")

        movie_obj.likes += 1
        username_obj.movies_liked.append(movie_obj)
        return f"{username} liked {movie_obj.title} movie."

    def dislike_movie(self, username: str, movie_obj):
        username_obj = self.searching_user_by_username(username)

        if movie_obj not in username_obj.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie_obj.title}!")

        movie_obj.likes -= 1
        username_obj.movies_liked.remove(movie_obj)
        return f"{username} disliked {movie_obj.title} movie."

    def display_movies(self):
        result = "No movies found."

        if self.movies_collection:
            result = sorted(self.movies_collection, key=lambda k: (-k.year, k.title()))
            result = '\n'.join([movie.details() for movie in result])

        return result

    def __str__(self):
        users = "All users: No users."
        if self.users_collection:
            users = "All users: " + ', '.join([user.username for user in self.users_collection])

        movies = "All movies: No movies."
        if self.movies_collection:
            movies = "All movies: " + ', '.join([movie.title for movie in self.movies_collection])

        return f"{users}\n{movies}"

    def searching_user_by_username(self, username):
        for user in self.users_collection:
            if user.username == username:
                return user
