from oop.all_exams.exam_10_december_2022.structure_and_func.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    def __init__(self, name: str, price: float):
        super().__init__(name, 250, price)

    def details(self):
        return f"Stolen {self.name}: 250g - {self.price:.2f}lv."
