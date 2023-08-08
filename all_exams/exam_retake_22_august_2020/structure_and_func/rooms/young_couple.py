from oop.all_exams.exam_retake_22_august_2020.structure_and_func.rooms.room import Room


class YoungCouple(Room):

    def __init__(self, family_name: str, salary_one, salary_two):
        budget = salary_one + salary_two
        members_count = 2
        super().__init__(family_name, budget, members_count)
        self.room_cost = 20
        self.appliances = [Room.add_tv(), Room.add_laptop(), Room.add_fridge()] * members_count
        self.__expenses = self.calculate_expenses(self.appliances, self.children)
