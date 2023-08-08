from oop.all_exams.exam_retake_22_august_2020.structure_and_func.rooms.room import Room


class OldCouple(Room):
    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        budget = pension_one + pension_two
        members_count = 2
        super().__init__(family_name, budget, members_count)
        self.room_cost = 15
        self.appliances = [Room.add_tv(), Room.add_stove(), Room.add_fridge()] * members_count
        self.__expenses = self.calculate_expenses(self.appliances, self.children)
