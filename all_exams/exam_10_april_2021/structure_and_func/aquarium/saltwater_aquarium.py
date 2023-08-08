from oop.all_exams.exam_10_april_2021.structure_and_func.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    FOR_TYPE_OF_FISH = "SaltwaterFish"

    def __init__(self, name: str):
        capacity = 25
        super().__init__(name, capacity)

    def add_fish(self, fish):
        if len(self.fish) >= self.capacity:
            return "Not enough capacity."

        self.fish.append(fish)
        return f"Successfully added {self.FOR_TYPE_OF_FISH} to {self.name}."
