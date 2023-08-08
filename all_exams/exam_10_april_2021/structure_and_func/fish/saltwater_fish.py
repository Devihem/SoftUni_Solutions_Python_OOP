from oop.all_exams.exam_10_april_2021.structure_and_func.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):

    def __init__(self, name: str, species: str, price: float):
        size = 5
        super().__init__(name, species, size, price)

    def eat(self):
        self.size += 2
