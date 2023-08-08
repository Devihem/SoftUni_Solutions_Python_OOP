class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.guild = "Unaffiliated"
        self.skills = {}  # {Magic: Mp}

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills.keys():
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return f"Skill already added"

    def player_info(self):
        skills_print = '\n'.join([f"==={sk} - {sk_mp}" for sk, sk_mp in self.skills.items()])
        return f"Name: {self.name}\n" \
               f"Guild: {self.guild}\n" \
               f"HP: {self.hp}\n"\
               f"MP: {self.mp}\n" \
               f"{skills_print}"



