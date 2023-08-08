from oop.all_exams.exam_retake_23_august_2021.structure_and_func.planet.planet_repository import PlanetRepository
from oop.all_exams.exam_retake_23_august_2021.structure_and_func.astronaut.astronaut_repository import AstronautRepository
from oop.all_exams.exam_retake_23_august_2021.structure_and_func.astronaut.geodesist import Geodesist
from oop.all_exams.exam_retake_23_august_2021.structure_and_func.astronaut.meteorologist import Meteorologist
from oop.all_exams.exam_retake_23_august_2021.structure_and_func.astronaut.biologist import Biologist
from oop.all_exams.exam_retake_23_august_2021.structure_and_func.planet.planet import Planet


class SpaceStation:
    ASTRONAUTS_TYPE = {"Biologist": Biologist, "Geodesist": Geodesist, "Meteorologist": Meteorologist}

    def __init__(self):
        self.astronaut_repository = AstronautRepository()
        self.planet_repository = PlanetRepository()
        self.missions_status = {"Successful": 0, "Unsuccessful": 0}

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in self.ASTRONAUTS_TYPE:
            raise Exception("Astronaut type is not valid!")

        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        created_astronaut_obj = self.ASTRONAUTS_TYPE[astronaut_type](name)
        self.astronaut_repository.add(created_astronaut_obj)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        created_planted_obj = Planet(name)
        created_planted_obj.items = items.split(', ')
        self.planet_repository.add(created_planted_obj)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        searched_astronaut = self.astronaut_repository.find_by_name(name)

        if not searched_astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(searched_astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name: str):
        if not self.planet_repository.find_by_name(planet_name):
            raise Exception("Invalid planet name!")

        selected_astronauts = self.astronauts_selection_method()
        if not selected_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        result = self.item_picking_from_planet(planet_name, selected_astronauts)
        return result

    def report(self):
        result = [f"{self.missions_status['Successful']} successful missions!",
                  f"{self.missions_status['Unsuccessful']} missions were not completed!",
                  "Astronauts' info:"]
        [result.append(str(astronaut)) for astronaut in self.astronaut_repository.astronauts]
        return '\n'.join(result)

    # Helpers -----------------------------------------------------------------------------

    def astronauts_selection_method(self):
        selected_astronauts = []
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.oxygen > 30:
                selected_astronauts.append(astronaut)

        selected_astronauts = sorted(selected_astronauts, key=lambda k: -k.oxygen)
        if len(selected_astronauts) > 5:
            selected_astronauts = selected_astronauts[:5]

        return selected_astronauts

    def item_picking_from_planet(self, planet_name, astronauts_team):

        current_planet = self.planet_repository.find_by_name(planet_name)

        for astronaut in astronauts_team:
            while True:
                current_item = current_planet.items.pop()
                current_astronaut_oxygen = astronaut.oxygen
                astronaut.breathe()

                if astronaut.oxygen < 0:
                    current_planet.items.append(current_item)
                    astronaut.oxygen = current_astronaut_oxygen
                    break

                astronaut.backpack.append(current_item)
                if not current_planet.items:

                    # Is not getting very clear what they want for {ASTRONAUT},  Number or Names or Else?
                    # Well it's ELSE  , how many "Step" on the planet
                    self.missions_status["Successful"] += 1
                    return f"Planet: {planet_name} was explored. {astronauts_team.index(astronaut) + 1} " \
                           f"astronauts participated in collecting items."

        self.missions_status["Unsuccessful"] += 1
        return "Mission is not completed."
