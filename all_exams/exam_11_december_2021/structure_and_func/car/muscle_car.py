from oop.all_exams.exam_11_december_2021.structure_and_func.car.car import Car


class MuscleCar(Car):
    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)

    def set_min_and_max_speed(self):
        self.MIN_SPEED_LIMIT = 250
        self.MAX_SPEED_LIMIT = 450
