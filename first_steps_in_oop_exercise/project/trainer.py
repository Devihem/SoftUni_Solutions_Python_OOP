from pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        # Simple to understand - method_______________________________________________

        # searched_pokemon = [x for x in self.pokemons if x.name == pokemon_name]
        # if self.pokemons:
        #     if searched_pokemon[0] in self.pokemons:
        #         self.pokemons.remove(searched_pokemon[0])
        #         return f"You have released {pokemon_name}"
        # return "Pokemon is not caught"

        # _____________________________________________________________________________

        # More advance method__________________________________________________________
        try:
            match = next(filter(lambda p: p.name == pokemon_name, self.pokemons))
            self.pokemons.remove(match)
            return f"You have released {pokemon_name}"

        except StopIteration:
            return "Pokemon is not caught"
        # _____________________________________________________________________________

    def trainer_data(self):
        pokemons_data = '\n'.join(f"- {p.pokemon_details()}" for p in self.pokemons)

        return f"Pokemon Trainer {self.name}" \
               f"\nPokemon count {len(self.pokemons)}" \
               f"\n{pokemons_data}"


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
third_pokemon = Pokemon("Huiomon", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(third_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
