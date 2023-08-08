class PlanetRepository:
    def __init__(self):
        self.planets = []

    def add(self, planet_obj):
        self.planets.append(planet_obj)

    def remove(self, planet_obj):
        self.planets.remove(planet_obj)

    def find_by_name(self,name):
        for planet in self.planets:
            if planet.name == name:
                return planet
