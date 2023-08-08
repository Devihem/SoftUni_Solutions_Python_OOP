from oop.all_exams.exam_16_august_2020.unit_test.project import Bird
from abc import ABC
from oop.all_exams.exam_16_august_2020.unit_test.project import Meat, Vegetable, Seed, Fruit


class Owl(Bird, ABC):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.food_list = [Meat]
        self.sound = "Hoot Hoot"
        self.weight_gain = 0.25

    def make_sound(self):
        return self.sound


class Hen(Bird, ABC):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.food_list = [Vegetable, Fruit, Meat, Seed]
        self.sound = "Cluck"
        self.weight_gain = 0.35

    def make_sound(self):
        return self.sound
