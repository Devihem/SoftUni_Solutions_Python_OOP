from employee import Employee
from person import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
