from oop.all_exams.exam_16_august_2020.structure_and_func.software.software import Software
from math import floor


class LightSoftware(Software):
    SOFTWARE_TYPE = 'Light'

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, self.SOFTWARE_TYPE, floor(capacity_consumption * 1.5), floor(memory_consumption / 2))
