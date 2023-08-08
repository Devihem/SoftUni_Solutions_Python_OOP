from oop.all_exams.exam_10_april_2022.structure_and_func.player import Player
from oop.all_exams.exam_10_april_2022.structure_and_func.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players: Player):
        currently_added_players = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                currently_added_players.append(player.name)
        else:
            return f"Successfully added: {', '.join(currently_added_players)}"

    def add_supply(self, *supplies: Supply):
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        searched_player = self.searching_player_by_name(player_name)

        # Check-1 - If there is no player - Ignore ! & Check-2 - If there is other supply type - Ignore !
        if searched_player and sustenance_type in ['Food', 'Drink']:

            if not searched_player.need_sustenance:  # Check-3 - If player don't need sustenance - Return msg
                return f"{searched_player.name} have enough stamina."

            searched_supply = self.searching_supply_by_type_reverse(sustenance_type)

            # Check-4 - If there is no more supply from this Type
            if searched_supply is None:
                raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

            if searched_player.stamina + searched_supply.energy > 100:
                searched_player.stamina = 100
            else:
                searched_player.stamina += searched_supply.energy

            return f"{searched_player.name} sustained successfully with {searched_supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):

        p1 = self.searching_player_by_name(first_player_name)
        p2 = self.searching_player_by_name(second_player_name)

        if p1.stamina == 0 or p2.stamina == 0:
            result = []
            if p1.stamina == 0:
                result.append(f"Player {p1.name} does not have enough stamina.")
            if p2.stamina == 0:
                result.append(f"Player {p2.name} does not have enough stamina.")
            return "\n".join(result)

        # Battle Phase
        players_battle_order = list(sorted([p1, p2], key=lambda k: k.stamina))

        # Round - 1
        first_attack = players_battle_order[0].stamina / 2
        first_defence = players_battle_order[1].stamina - first_attack
        players_battle_order[1].stamina = first_defence

        # Round - 2
        second_attack = players_battle_order[1].stamina / 2
        second_defence = players_battle_order[0].stamina - second_attack
        if second_defence <= 0:
            players_battle_order[0].stamina = 0
            return f"Winner: {players_battle_order[1].name}"
        players_battle_order[0].stamina = second_defence

        winner = list(sorted(players_battle_order, key=lambda k: k.stamina))[1]
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            subtract_stamina = player.age * 2

            if player.stamina - subtract_stamina < 0:
                player.stamina = 0
            else:
                player.stamina -= subtract_stamina

        # Food and drink first or all Food first then all drink ?
        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []
        for player in self.players:
            result.append(str(player))
        for supply in self.supplies:
            result.append(supply.details())

        return '\n'.join(result)

    # HELPERS ----------------------------------------------------------------------------
    def searching_player_by_name(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def searching_supply_by_type_reverse(self, supply_type):
        for supply_index in range(len(self.supplies) - 1, -1, -1):
            if self.supplies[supply_index].type == supply_type:
                return self.supplies.pop(supply_index)
