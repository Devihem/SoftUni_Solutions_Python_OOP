from encapsulation_exercise.wild_cat_zoo.animal import Animal


class Tiger(Animal):
    PERSONAL_MONEY_TO_CARE = 45

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, self.PERSONAL_MONEY_TO_CARE)
