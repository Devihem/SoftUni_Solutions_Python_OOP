from math import floor
from oop.all_exams.exam_16_august_2020.structure_and_func.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    HARDWARE_TYPE = 'Heavy'

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, self.HARDWARE_TYPE, capacity * 2, floor(memory * 0.75))