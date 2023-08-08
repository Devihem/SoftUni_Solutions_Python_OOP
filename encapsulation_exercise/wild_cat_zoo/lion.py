from encapsulation_exercise.wild_cat_zoo.animal import Animal


class Lion(Animal):
    PERSONAL_MONEY_TO_CARE = 50

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, self.PERSONAL_MONEY_TO_CARE)
