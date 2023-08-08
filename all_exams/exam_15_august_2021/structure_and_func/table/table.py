from abc import ABC, abstractmethod


class Table(ABC):
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    @abstractmethod
    def table_type(self):
        return ...

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self.__capacity = value

    def reserve(self, number_of_people: int):
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, baked_food_obj):
        self.food_orders.append(baked_food_obj)

    def order_drink(self, drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        total_food_price = sum([food.price for food in self.food_orders])
        total_drinks_price = sum([drink.price for drink in self.drink_orders])
        return total_drinks_price + total_food_price

    def clear(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}\n" \
                   f"Type: {self.table_type()}\n" \
                   f"Capacity: {self.capacity}"
