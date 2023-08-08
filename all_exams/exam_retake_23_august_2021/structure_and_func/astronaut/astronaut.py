from abc import ABC, abstractmethod


class Astronaut(ABC):
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    @abstractmethod
    def breathe(self):
        pass

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    def __repr__(self):
        backpack_result = ', '.join([items for items in self.backpack])
        if not backpack_result:
            backpack_result = 'none'

        return f'Name: {self.name}\n' \
               f'Oxygen: {self.oxygen}\n' \
               f'Backpack items: {backpack_result}'
