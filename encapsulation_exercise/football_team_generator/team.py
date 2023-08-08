from encapsulation_exercise.football_team_generator.player import Player


class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        for searched_player in self.__players:
            if searched_player.name == player_name:
                removed_player = searched_player
                self.__players.remove(removed_player)
                return removed_player
        return f"Player {player_name} not found"
