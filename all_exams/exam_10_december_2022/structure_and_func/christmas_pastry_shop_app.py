from oop.all_exams.exam_10_december_2022.structure_and_func.booths.open_booth import OpenBooth
from oop.all_exams.exam_10_december_2022.structure_and_func.booths.private_booth import PrivateBooth
from oop.all_exams.exam_10_december_2022.structure_and_func.delicacies.stolen import Stolen
from oop.all_exams.exam_10_december_2022.structure_and_func.delicacies.gingerbread import Gingerbread


class ChristmasPastryShopApp:
    VALID_DELICACY = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    VALID_BOOTH = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths = []  # obj
        self.delicacies = []  # obj
        self.income = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if self.search_for_delicacy_by_name(name):
            raise Exception(f"{name} already exists!")

        if type_delicacy not in self.VALID_DELICACY:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        created_delicacy = self.VALID_DELICACY[type_delicacy](name, price)
        self.delicacies.append(created_delicacy)

        return f"Added delicacy {name} - {type(created_delicacy).__name__} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if self.search_for_booth_by_number_name(booth_number):
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.VALID_BOOTH:
            raise Exception(f"{type_booth} is not a valid booth!")

        created_booth = self.VALID_BOOTH[type_booth](booth_number, capacity)
        self.booths.append(created_booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
        else:
            raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):

        booth_obj = self.search_for_booth_by_number_name(booth_number)
        if not booth_obj:
            raise Exception(f"Could not find booth {booth_number}!")

        delicacy_obj = self.search_for_delicacy_by_name(delicacy_name)
        if not delicacy_obj:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth_obj.delicacy_orders.append(delicacy_obj)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth_obj = self.search_for_booth_by_number_name(booth_number)

        booth_bill = sum([delicacy.price for delicacy in booth_obj.delicacy_orders]) + booth_obj.price_for_reservation

        booth_obj.price_for_reservation = 0
        booth_obj.delicacy_orders = []
        booth_obj.is_reserved = False

        self.income += booth_bill
        return f"Booth {booth_number}:\nBill: {booth_bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    # HELPERS------------------------------------------------------------------

    def search_for_delicacy_by_name(self, delicacy_name):
        for delicacy in self.delicacies:
            if delicacy.name == delicacy_name:
                return delicacy

    def search_for_booth_by_number_name(self, number_name):
        for booth in self.booths:
            if booth.booth_number == number_name:
                return booth
