from oop.all_exams.exam_14_august_2022.structure_and_func.horse_specification.appaloosa import Appaloosa
from oop.all_exams.exam_14_august_2022.structure_and_func.horse_specification.thoroughbred import Thoroughbred
from oop.all_exams.exam_14_august_2022.structure_and_func.horse_race import HorseRace
from oop.all_exams.exam_14_august_2022.structure_and_func.jockey import Jockey


class HorseRaceApp:
    AVAILABLE_HORSES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses = []  # obj
        self.jockeys = []  # obj
        self.horse_races = []  # obj
        self.already_created_race_types = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        for horse in self.horses:
            if horse.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.AVAILABLE_HORSES:
            created_horse = self.AVAILABLE_HORSES[horse_type](horse_name, horse_speed)
            self.horses.append(created_horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")

        created_jockey = Jockey(jockey_name, age)
        self.jockeys.append(created_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        for race in self.horse_races:
            if race.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")

        created_horse_race = HorseRace(race_type)
        self.horse_races.append(created_horse_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):

        try:
            jockey_obj = next(filter(lambda jockey: jockey.name == jockey_name, self.jockeys))
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        index_counter = len(self.horses)
        for horse in self.horses[::-1]:
            index_counter -= 1

            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                break
        else:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey_obj.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey_obj.horse = self.horses[index_counter]
        self.horses[index_counter].is_taken = True
        return f"Jockey {jockey_name} will ride the horse {self.horses[index_counter].name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        for race in self.horse_races:
            if race.race_type == race_type:
                race_obj = race
                break
        else:
            raise Exception(f"Race {race_type} could not be found!")

        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                jockey_obj = jockey
                break
        else:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey_obj.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        for jockey in race_obj.jockeys:
            if jockey.name == jockey_name:
                return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race_obj.jockeys.append(jockey_obj)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):

        for race in self.horse_races:
            if race.race_type == race_type:
                race_obj = race
                break
        else:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race_obj.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        best_race_speed = float("-inf")
        best_racer_obj = ''
        for jockey in race_obj.jockeys:
            if jockey.horse.speed > best_race_speed:
                best_racer_obj = jockey
                best_race_speed = jockey.horse.speed

        return f"The winner of the {race_type} race, with a speed of {best_race_speed}km/h is {best_racer_obj.name}!" \
               f" Winner's horse: {best_racer_obj.horse.name}."
