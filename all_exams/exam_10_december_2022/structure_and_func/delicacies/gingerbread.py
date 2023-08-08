from oop.all_exams.exam_10_december_2022.structure_and_func.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    def __init__(self, name: str, price: float):
        super().__init__(name, 200, price)

    def details(self):
        return f"Gingerbread {self.name}: 200g - {self.price:.2f}lv."
