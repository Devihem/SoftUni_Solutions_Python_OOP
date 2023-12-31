from all_exams.exam_10_april_2022.structure_and_func.supply.supply import Supply


class Food(Supply):
    def __init__(self, name: str, energy=25):
        super().__init__(name, energy)
        self.type = 'Food'

    def details(self):
        return f"{self.type}: {self.name}, {self.energy}"
