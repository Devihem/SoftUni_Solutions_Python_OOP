from oop.all_exams.exam_18_april_2023.e_drive_rent.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    MAX_MILEAGE = 450.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, PassengerCar.MAX_MILEAGE)

    def drive(self, mileage: float):
        drained_battery_units = round(mileage / (self.MAX_MILEAGE / 100))
        self.battery_level -= drained_battery_units
