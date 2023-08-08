from oop.all_exams.exam_retake_22_august_2020.structure_and_func.rooms.room import Room


class YoungCoupleWithChildren(Room):
    APPLIANCES_LIST = [Room.add_tv(), Room.add_laptop(), Room.add_fridge()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        budget = salary_one + salary_two
        members_count = 2 + len(children)
        super().__init__(family_name, budget, members_count)
        self.children = list(children)
        self.room_cost = 30
        self.appliances = [Room.add_tv(), Room.add_laptop(), Room.add_fridge()] * members_count
        self.__expenses = self.calculate_expenses(self.appliances, self.children)
