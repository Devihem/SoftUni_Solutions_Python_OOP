class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []  # obj
        self.bill = 0.0
        self.ongoing_shopping_dict = {}

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value: str):
        if value[0] != "0" or len(value) != 10 or not value.isnumeric():
            raise ValueError("Invalid phone number!")

        self.__phone_number = value
