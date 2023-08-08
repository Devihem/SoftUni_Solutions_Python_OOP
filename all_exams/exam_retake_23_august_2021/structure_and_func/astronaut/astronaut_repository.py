class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut_obj):
        self.astronauts.append(astronaut_obj)

    def remove(self, astronaut_obj):
        self.astronauts.remove(astronaut_obj)

    def find_by_name(self, name):
        for astronaut in self.astronauts:
            if astronaut.name == name:
                return astronaut
