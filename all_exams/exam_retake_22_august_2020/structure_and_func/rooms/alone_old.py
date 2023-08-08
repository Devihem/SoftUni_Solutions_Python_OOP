from oop.all_exams.exam_retake_22_august_2020.structure_and_func.rooms.room import Room


class AloneOld(Room):

    def __init__(self, family_name: str, pension: float):
        budget = pension
        members_count = 1
        super().__init__(family_name, budget, members_count)
        self.room_cost = 10
        self.appliances = [] * members_count
        self.__expenses = self.calculate_expenses(self.appliances, self.children)
