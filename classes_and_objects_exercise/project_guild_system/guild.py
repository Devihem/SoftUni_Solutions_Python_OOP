from player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == "Unaffiliated" and player not in self.players:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

        elif player in self.players:
            return f"Player {player.name} is already in the guild."

        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        for player_loc_data in self.players:
            if player_loc_data.name == player_name:
                self.players.remove(player_loc_data)
                player_loc_data.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."
        else:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        players_in_guild_print = '\n'.join([f"{print_player.player_info()}" for print_player in self.players])
        return f"Guild: {self.name}\n{players_in_guild_print}"

x = Player()