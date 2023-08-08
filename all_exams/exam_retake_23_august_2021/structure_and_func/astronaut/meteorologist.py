from oop.all_exams.exam_retake_23_august_2021.structure_and_func.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    def __init__(self, name: str):
        oxygen = 90
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= 15
