from oop.all_exams.exam_11_december_2021.structure_and_func.car.muscle_car import MuscleCar
from oop.all_exams.exam_11_december_2021.structure_and_func.car.sports_car import SportsCar
from oop.all_exams.exam_11_december_2021.structure_and_func.race import Race
from oop.all_exams.exam_11_december_2021.structure_and_func.driver import Driver


class Controller:
    AVAILABLE_CARS = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if self.searching_for_car_by_name(model):
            raise Exception(f"Car {model} is already created!")

        if car_type in self.AVAILABLE_CARS:
            created_car = self.AVAILABLE_CARS[car_type](model, speed_limit)
            self.cars.append(created_car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if self.searching_for_drivers_by_name(driver_name):
            raise Exception(f"Driver {driver_name} is already created!")

        created_driver_obj = Driver(driver_name)
        self.drivers.append(created_driver_obj)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if self.searching_for_race_by_name(race_name):
            raise Exception(f"Race {race_name} is already created!")

        created_race_obj = Race(race_name)
        self.races.append(created_race_obj)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver_obj = self.searching_for_drivers_by_name(driver_name)
        if not driver_obj:
            raise Exception(f"Driver {driver_name} could not be found!")

        car_obj = self.searching_for_available_car_type_reverse(car_type)
        if not car_obj:
            raise Exception(f"Car {car_type} could not be found!")

        if driver_obj.car:
            # Old car is free
            old_car_model = driver_obj.car.model
            driver_obj.car.is_taken = False

            # New car is taken
            car_obj.is_taken = True

            # Old car is replaced with new car
            driver_obj.car = car_obj
            return f"Driver {driver_name} changed his car from {old_car_model} to {car_obj.model}."

        else:
            driver_obj.car = car_obj
            car_obj.is_taken = True
            return f"Driver {driver_name} chose the car {car_obj.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race_obj = self.searching_for_race_by_name(race_name)
        if not race_obj:
            raise Exception(f"Race {race_name} could not be found!")

        driver_obj = self.searching_for_drivers_by_name(driver_name)
        if not driver_obj:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver_obj.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver_obj in race_obj.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."
        else:
            race_obj.drivers.append(driver_obj)
            return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race_obj = self.searching_for_race_by_name(race_name)
        if not race_obj:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race_obj.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        racers_by_speed = sorted(race_obj.drivers, key=lambda k: -k.car.speed_limit)

        finish_result_print = []

        # racer = driver_obj ( but in race )
        for racer in racers_by_speed[:3]:
            racer.number_of_wins += 1
            finish_result_print.append(
                f"Driver {racer.name} wins the {race_name} race with a speed of {racer.car.speed_limit}.")

        return '\n'.join(finish_result_print)

    # HELPERS ----------------------------------------------------------------------------------------

    def searching_for_car_by_name(self, car_model):
        for car in self.cars:
            if car.model == car_model:
                return car

    def searching_for_drivers_by_name(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver

    def searching_for_race_by_name(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race

    def searching_for_available_car_type_reverse(self, car_type):
        for car in self.cars[::-1]:
            if car.__class__.__name__ == car_type:
                if not car.is_taken:
                    return car
