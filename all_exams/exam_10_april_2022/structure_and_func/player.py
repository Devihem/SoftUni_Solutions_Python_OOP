class Player:
    ALL_PLAYERS_NAME = []

    def __init__(self, name: str, age: int, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def need_sustenance(self):
        return True if self.stamina < 100 else False

    # Name Get/Set
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name not valid!")

        if value in Player.ALL_PLAYERS_NAME:
            raise Exception(f"Name {value} is already used!")

        Player.ALL_PLAYERS_NAME.append(value)
        self.__name = value

    # Age Get/Set
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    # Stamina Get/Set
    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if not 0 <= value <= 100:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"