from oop.all_exams.exam_retake_22_august_2020.structure_and_func.appliances.fridge import Fridge
from oop.all_exams.exam_retake_22_august_2020.structure_and_func.appliances.laptop import Laptop
from oop.all_exams.exam_retake_22_august_2020.structure_and_func.appliances.stove import Stove
from oop.all_exams.exam_retake_22_august_2020.structure_and_func.appliances.tv import TV


class Room:
    def __init__(self, family_name: str, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []  # Obj list
        self.expenses = 0  # If it is set to a negative number, raise ValueError

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if float(value) < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        total_expenses = 0
        for units_list in args:
            for unit in units_list:
                total_expenses += unit.get_monthly_expense()
        # Bad patter design / the task force you to make it /
        self.expenses = total_expenses

    # Helpers -------------------------------------------------------------------

    @staticmethod
    def add_tv():
        return TV()

    @staticmethod
    def add_fridge():
        return Fridge()

    @staticmethod
    def add_laptop():
        return Laptop()

    @staticmethod
    def add_stove():
        return Stove()