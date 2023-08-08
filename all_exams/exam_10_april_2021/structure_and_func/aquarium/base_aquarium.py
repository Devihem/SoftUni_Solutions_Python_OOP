from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity  # number of fish , aquarium can have
        self.decorations = []  # obj
        self.fish = []  # obj

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum([item.comfort for item in self.decorations])

    @abstractmethod
    def add_fish(self, fish):
        pass

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        [fish.eat() for fish in self.fish]

    def __str__(self):
        fish_names = [fish.name for fish in self.fish]

        if not fish_names:
            fish_names = ['none']

        return f"{self.name}:\n" \
               f"Fish: {' '.join(fish_names)}\n" \
               f"Decorations: {len(self.decorations)}\n" \
               f"Comfort: {self.calculate_comfort()}"
