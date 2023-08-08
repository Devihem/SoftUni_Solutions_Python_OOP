from encapsulation_exercise.pizza_maker.dough import Dough
from encapsulation_exercise.pizza_maker.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings = {}  # Topping Type: Topping weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 1:
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        if value < 1:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self.__max_number_of_toppings = value

    def add_topping(self, topping: Topping):
        if self.__max_number_of_toppings > len(self.toppings.keys()):
            if topping.topping_type not in self.toppings.keys():
                self.toppings[topping.topping_type] = 0
            self.toppings[topping.topping_type] += topping.weight

        else:
            raise ValueError("Not enough space for another topping")

    def calculate_total_weight(self):
        total_toppings_weight = sum(self.toppings.values())
        return self.dough.weight + total_toppings_weight
