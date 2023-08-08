from oop.all_exams.exam_retake_19_december_2022.structure_and_func.band_members.musician import Musician


class Drummer(Musician):
    POSSIBLE_SKILLS = ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"]

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
