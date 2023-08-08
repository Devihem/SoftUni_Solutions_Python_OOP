from oop.all_exams.exam_10_april_2021.structure_and_func.aquarium.freshwater_aquarium import FreshwaterAquarium
from oop.all_exams.exam_10_april_2021.structure_and_func.aquarium.saltwater_aquarium import SaltwaterAquarium
from oop.all_exams.exam_10_april_2021.structure_and_func.decoration.plant import Plant
from oop.all_exams.exam_10_april_2021.structure_and_func.decoration.ornament import Ornament
from oop.all_exams.exam_10_april_2021.structure_and_func.fish.saltwater_fish import SaltwaterFish
from oop.all_exams.exam_10_april_2021.structure_and_func.fish.freshwater_fish import FreshwaterFish
from oop.all_exams.exam_10_april_2021.structure_and_func.decoration.decoration_repository import DecorationRepository


class Controller:
    TYPE_OF_AQUARIUMS = {"FreshwaterAquarium": FreshwaterAquarium, "SaltwaterAquarium": SaltwaterAquarium}
    TYPE_OF_DECORATION = {"Ornament": Ornament, "Plant": Plant}
    TYPE_OF_FISHES = {"FreshwaterFish": FreshwaterFish, "SaltwaterFish": SaltwaterFish}

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.TYPE_OF_AQUARIUMS:
            return "Invalid aquarium type."

        self.aquariums.append(self.TYPE_OF_AQUARIUMS[aquarium_type](aquarium_name))
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in self.TYPE_OF_DECORATION:
            return "Invalid decoration type."

        # First check in dict with types, then use to ADD from decoration file
        result = self.TYPE_OF_DECORATION[decoration_type]()
        self.decorations_repository.add(result)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = self.searching_for_aquarium(aquarium_name)
        current_decoration = self.decorations_repository.find_by_type(decoration_type)

        if current_decoration == "None" or not aquarium:
            return f"There isn't a decoration of type {decoration_type}."

        self.decorations_repository.decorations.remove(current_decoration)
        aquarium.add_decoration(current_decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in self.TYPE_OF_FISHES:
            return f"There isn't a fish of type {fish_type}."

        aquarium = self.searching_for_aquarium(aquarium_name)

        if fish_type != aquarium.FOR_TYPE_OF_FISH:
            return "Water not suitable."

        created_fish_obj = self.TYPE_OF_FISHES[fish_type](fish_name, fish_species, price)
        return aquarium.add_fish(created_fish_obj)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.searching_for_aquarium(aquarium_name)
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.searching_for_aquarium(aquarium_name)
        fishes_value = sum([fish.price for fish in aquarium.fish])
        decoration_value = sum([decor.price for decor in aquarium.decorations])
        aquarium_value = fishes_value + decoration_value

        return f"The value of Aquarium {aquarium_name} is {aquarium_value:.2f}."

    def report(self):
        result = [str(aquarium) for aquarium in self.aquariums]
        return "\n".join(result)

    # HELPERS

    def searching_for_aquarium(self, aq_name):
        for aq in self.aquariums:
            if aq_name == aq.name:
                return aq
