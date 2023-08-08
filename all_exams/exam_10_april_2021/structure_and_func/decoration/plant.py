from oop.all_exams.exam_10_april_2021.structure_and_func.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    def __init__(self):
        super().__init__(comfort=5, price=10)
