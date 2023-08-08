from oop.all_exams.exam_10_december_2022.structure_and_func.booths.booth import Booth


class PrivateBooth(Booth):
    PRICE_PER_PERSON_RESERVATION = 3.5

    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        self.price_for_reservation = number_of_people * self.PRICE_PER_PERSON_RESERVATION
        self.is_reserved = True
