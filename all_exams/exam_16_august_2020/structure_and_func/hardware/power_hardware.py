from math import floor
from oop.all_exams.exam_16_august_2020.structure_and_func.hardware.hardware import Hardware


class PowerHardware(Hardware):
    HARDWARE_TYPE = 'Power'

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, self.HARDWARE_TYPE, floor(capacity * 0.25), floor(memory * 1.75))
