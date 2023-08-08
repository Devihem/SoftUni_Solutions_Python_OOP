from oop.all_exams.exam_14_august_2022.structure_and_func.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        train_speed_value = 3
        if self.speed + train_speed_value > self.MAX_SPEED:
            self.speed = self.MAX_SPEED - train_speed_value

        self.speed += train_speed_value
