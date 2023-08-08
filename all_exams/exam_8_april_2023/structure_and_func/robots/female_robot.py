from oop.all_exams.exam_8_april_2023.structure_and_func.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, 7)

    def eating(self):
        self.weight += 1
