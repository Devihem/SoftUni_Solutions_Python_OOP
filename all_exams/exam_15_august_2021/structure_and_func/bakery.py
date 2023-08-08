from oop.all_exams.exam_15_august_2021.structure_and_func.baked_food.bread import Bread
from oop.all_exams.exam_15_august_2021.structure_and_func.baked_food.cake import Cake
from oop.all_exams.exam_15_august_2021.structure_and_func.drink.tea import Tea
from oop.all_exams.exam_15_august_2021.structure_and_func.drink.water import Water
from oop.all_exams.exam_15_august_2021.structure_and_func.table.inside_table import InsideTable
from oop.all_exams.exam_15_august_2021.structure_and_func.table.outside_table import OutsideTable


class Bakery:
    AVAILABLE_FOODS = {"Bread": Bread, "Cake": Cake}
    AVAILABLE_DRINKS = {"Tea": Tea, "Water": Water}
    AVAILABLE_TABLES = {"InsideTable": InsideTable, "OutsideTable": OutsideTable}

    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, food_name: str, food_price: float):
        if self.search_food_by_name(food_name):
            raise Exception(f"{food_type} {food_name} is already in the menu!")

        created_food = self.AVAILABLE_FOODS[food_type](food_name, food_price)
        self.food_menu.append(created_food)
        return f"Added {food_name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, drink_name: str, portion: float, brand: str):
        if self.search_drink_by_name(drink_name):
            raise Exception(f"{drink_type} {drink_name} is already in the menu!")

        created_drink = self.AVAILABLE_DRINKS[drink_type](drink_name, portion, brand)
        self.drinks_menu.append(created_drink)
        return f"Added {drink_name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if self.search_table_by_number(table_number):
            raise Exception(f"Table {table_number} is already in the bakery!")

        created_table = self.AVAILABLE_TABLES[table_type](table_number, capacity)
        self.tables_repository.append(created_table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if table.capacity >= number_of_people and not table.is_reserved:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *foods_name_args):
        searched_table = self.search_table_by_number(table_number)
        if not searched_table:
            return f"Could not find table {table_number}"

        ordered_food_print = [f"Table {table_number} ordered:"]
        not_ordered_food_print = [f"{self.name} does not have in the menu:"]

        for food_name in foods_name_args:
            current_food_obj = self.search_food_by_name(food_name)
            if current_food_obj:
                searched_table.order_food(current_food_obj)
                ordered_food_print.append(str(current_food_obj))
            else:
                not_ordered_food_print.append(food_name)

        final_print = ordered_food_print + not_ordered_food_print
        return '\n'.join(final_print)

    def order_drink(self, table_number: int, *drinks_name_args):
        searched_table = self.search_table_by_number(table_number)
        if not searched_table:
            return f"Could not find table {table_number}"

        ordered_drink_print = [f"Table {table_number} ordered:"]
        not_ordered_drink_print = [f"{self.name} does not have in the menu:"]

        for drink_name in drinks_name_args:
            current_drink_obj = self.search_drink_by_name(drink_name)
            if current_drink_obj:
                searched_table.order_drink(current_drink_obj)
                ordered_drink_print.append(str(current_drink_obj))
            else:
                not_ordered_drink_print.append(drink_name)

        final_print = ordered_drink_print + not_ordered_drink_print
        return '\n'.join(final_print)

    def leave_table(self, table_number: int):
        searched_table = self.search_table_by_number(table_number)
        income_from_table = searched_table.get_bill()
        self.total_income += income_from_table
        searched_table.clear()
        return f"Table: {table_number}\n" \
               f"Bill: {income_from_table:.2f}"

    def get_free_tables_info(self):
        result = []
        for table in self.tables_repository:
            if not table.is_reserved:
                result.append(table.free_table_info())
        return "\n".join(result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    # Helper   -----------------------------------------------------------------------

    def search_food_by_name(self, food_name):
        for food in self.food_menu:
            if food.name == food_name:
                return food

    def search_drink_by_name(self, drink_name):
        for drink in self.drinks_menu:
            if drink.name == drink_name:
                return drink

    def search_table_by_number(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table
