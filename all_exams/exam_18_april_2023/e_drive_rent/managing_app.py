import copy

from oop.all_exams.exam_18_april_2023.e_drive_rent.user import User
from oop.all_exams.exam_18_april_2023.e_drive_rent.route import Route
from oop.all_exams.exam_18_april_2023.e_drive_rent.vehicles.cargo_van import CargoVan
from oop.all_exams.exam_18_april_2023.e_drive_rent.vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."
        else:
            self.users.append(User(first_name, last_name, driving_license_number))
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ["PassengerCar", "CargoVan"]:
            return f"Vehicle type {vehicle_type} is inaccessible."

        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."
        else:
            if vehicle_type == "PassengerCar":
                self.vehicles.append(PassengerCar(brand, model, license_plate_number))
            elif vehicle_type == "CargoVan":
                self.vehicles.append(CargoVan(brand, model, license_plate_number))

            return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point:
                if route.length == length:
                    return f"{start_point}/{end_point} - {length} km had already been added to our platform."
                elif route.length < length:
                    return f"{start_point}/{end_point} shorter route had already been added to our platform."
                elif route.length > length:
                    route.is_locked = True
        else:
            # Trying to go cheap with the ID generator ( its working )
            self.routes.append(Route(start_point, end_point, length, len(self.routes) + 1))
            return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    # Testing the return if it's REAL string or obj - test number -5
    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        # 100% True - Driving_license, Plate_number , Route_id , Battery enough allays

        # USER
        searched_user = [user for user in self.users if user.driving_license_number == driving_license_number][0]
        if searched_user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        # VEHICLE
        searched_vehicle = [vehic for vehic in self.vehicles if vehic.license_plate_number == license_plate_number][0]
        if searched_vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        # ROUTE
        searched_route = [route for route in self.routes if route.route_id == route_id][0]
        if searched_route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        # DRIVING
        searched_vehicle.drive(searched_route.length)

        if is_accident_happened:
            searched_vehicle.is_damaged = True
            searched_user.decrease_rating()
        else:
            searched_user.increase_rating()

        return str(searched_vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicle = []
        repaired = 0
        for vehicle in self.vehicles:
            if vehicle.is_damaged:
                damaged_vehicle.append(vehicle)

        if damaged_vehicle:
            damaged_vehicle = sorted(damaged_vehicle, key=lambda k: (k.brand, k.model))

        for repair in range(count):
            if damaged_vehicle:
                repaired += 1

                damaged_vehicle[0].change_status()
                damaged_vehicle[0].recharge()
                damaged_vehicle.pop(0)
            else:
                break

        return f"{repaired} vehicles were successfully repaired!"

    def users_report(self):
        report_users = copy.copy(self.users)
        report_users = sorted(report_users, key=lambda k: -k.rating)
        print_result = '\n'.join([str(x) for x in report_users])

        return f"*** E-Drive-Rent ***\n{print_result}"
