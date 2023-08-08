from oop.all_exams.exam_16_august_2020.unit_test.project import Person


class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)