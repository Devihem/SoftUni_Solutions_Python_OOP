from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    @abstractmethod
    def calculate_revenue_after_race(self, race_pos: int):
        pass

    def revenue_calculator(self, race_pos):
        sponsor_money = 0
        for positions in self.sponsors_reward.values():
            for pos in positions:
                if race_pos <= pos:
                    sponsor_money += positions[pos]
                    break

        revenue = self.expenses_per_race + sponsor_money
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
