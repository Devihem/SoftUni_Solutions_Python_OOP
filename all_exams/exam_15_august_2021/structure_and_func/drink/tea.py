from oop.all_exams.exam_15_august_2021.structure_and_func.drink.drink import Drink


class Tea(Drink):
    def __init__(self, name: str, portion: float, brand: str):
        price = 2.50
        super().__init__(name, portion, price, brand)