from oop.all_exams.exam_18_april_2023.e_drive_rent.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, CargoVan.MAX_MILEAGE)

    # Working - Test 14 in Judge
    def drive(self, mileage: float):
        drained_battery_units = round(mileage / (self.MAX_MILEAGE / 100))
        extra_battery_drain = 5
        self.battery_level -= drained_battery_units + extra_battery_drain
