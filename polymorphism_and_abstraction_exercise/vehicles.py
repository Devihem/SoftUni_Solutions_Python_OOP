from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, drive_distance):
        pass

    @abstractmethod
    def refuel(self, refuel):
        pass


class Car(Vehicle):

    def drive(self, drive_distance):
        ac_consumption = 0.9
        current_consumption = self.fuel_consumption + ac_consumption
        if self.fuel_quantity / current_consumption >= drive_distance:
            self.fuel_quantity -= drive_distance * current_consumption

    def refuel(self, refuel):
        self.fuel_quantity += refuel


class Truck(Vehicle):

    def drive(self, drive_distance):
        ac_consumption = 1.6
        current_consumption = self.fuel_consumption + ac_consumption
        if self.fuel_quantity / current_consumption >= drive_distance:
            self.fuel_quantity -= drive_distance * current_consumption

    def refuel(self, refuel):
        self.fuel_quantity += refuel * 0.95

