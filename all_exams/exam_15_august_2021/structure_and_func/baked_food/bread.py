from oop.all_exams.exam_15_august_2021.structure_and_func.baked_food.baked_food import BakedFood


class Bread(BakedFood):

    def __init__(self, name: str, price: float):
        portion = 200
        super().__init__(name, portion, price)
