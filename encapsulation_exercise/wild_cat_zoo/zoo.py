from typing import List


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[str] = []
        self.workers: List[str] = []

    def add_animal(self, animal, price: int):
        if self.__animal_capacity > len(self.animals):
            if self.__budget >= price:
                self.__budget -= price
                self.animals.append(animal)

                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)

            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for searched_worker in self.workers:
            if searched_worker.name == worker_name:
                self.workers.remove(searched_worker)
                return f"{searched_worker.name} fired successfully"
        return f"There is no {worker_name} in the zoo"

        # Next Method
        # try:
        #     worker = next(filter(lambda w: w.name == worker_name, self.workers))
        # except StopIteration:
        #     return f"There is no {worker_name} in the zoo"
    def pay_workers(self):
        total_salary_cost = sum([worker_obj.salary for worker_obj in self.workers])
        if self.__budget >= total_salary_cost:
            self.__budget -= total_salary_cost

            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_tend_cost = sum([animal_obj.money_for_care for animal_obj in self.animals])
        if self.__budget >= total_tend_cost:
            self.__budget -= total_tend_cost

            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        animals_dict = {}
        for animal_in_zoo in self.animals:
            animal_type = animal_in_zoo.__class__.__name__
            animal_type_repr = f"{animal_in_zoo}"
            if animal_type not in animals_dict:
                animals_dict[animal_type] = []
            animals_dict[animal_type].append(animal_type_repr)

        result = [
            f"You have {len(self.animals)} animals",
            f"----- {len(animals_dict['Lion'])} Lions:",
            *animals_dict['Lion'],
            f"----- {len(animals_dict['Tiger'])} Tigers:",
            *animals_dict['Tiger'],
            f"----- {len(animals_dict['Cheetah'])} Cheetahs:",
            *animals_dict['Cheetah']
        ]
        return '\n'.join(result)

    def workers_status(self):
        workers_dict = {}
        for worker_in_zoo in self.workers:
            worker_type = worker_in_zoo.__class__.__name__
            worker_type_repr = f"{worker_in_zoo}"
            if worker_type not in workers_dict:
                workers_dict[worker_type] = []
            workers_dict[worker_type].append(worker_type_repr)

        result = [
            f"You have {len(self.workers)} workers",
            f"----- {len(workers_dict['Keeper'])} Keepers:",
            *workers_dict['Keeper'],
            f"----- {len(workers_dict['Caretaker'])} Caretakers:",
            *workers_dict['Caretaker'],
            f"----- {len(workers_dict['Vet'])} Vets:",
            *workers_dict['Vet']
        ]
        return '\n'.join(result)
