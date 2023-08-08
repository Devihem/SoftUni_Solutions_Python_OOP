from oop.all_exams.exam_retake_19_december_2022.structure_and_func.band_members.musician import Musician


class Guitarist(Musician):
    POSSIBLE_SKILLS = ["play metal", "play rock", "play jazz"]

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
