from oop.all_exams.exam_retake_22_august_2022.structure_and_func.meals.meal import Meal


class Starter(Meal):
    def __init__(self, name: str, price: float, quantity=60):
        super().__init__(name, price, quantity)

    def details(self):
        return f"Starter {self.name}: {self.price:.2f}lv/piece"
