from oop.all_exams.exam_8_april_2023.structure_and_func.robots.male_robot import MaleRobot
from oop.all_exams.exam_8_april_2023.structure_and_func.robots.female_robot import FemaleRobot
from oop.all_exams.exam_8_april_2023.structure_and_func.services.main_service import MainService
from oop.all_exams.exam_8_april_2023.structure_and_func.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICE = {"MainService": MainService, "SecondaryService": SecondaryService}
    VALID_ROBOTS = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots = []  # obj
        self.services = []  # obj

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICE:
            raise Exception("Invalid service type!")

        created_service = self.VALID_SERVICE[service_type](name)
        self.services.append(created_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOTS:
            raise Exception("Invalid robot type!")

        created_robot = self.VALID_ROBOTS[robot_type](name, kind, price)
        self.robots.append(created_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot_obj = self.searching_for_robot_by_name(robot_name)
        service_obj = self.searching_for_service_by_name(service_name)

        if (type(robot_obj).__name__ == "MaleRobot" and type(service_obj).__name__ == "SecondaryService") \
                or (type(robot_obj).__name__ == "FemaleRobot" and type(service_obj).__name__ == "MainService"):
            return "Unsuitable service."

        if service_obj.capacity <= len(service_obj.robots):
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot_obj)
        service_obj.robots.append(robot_obj)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service_obj = self.searching_for_service_by_name(service_name)

        for robot in service_obj.robots:
            if robot.name == robot_name:
                robot_obj = robot
                break
        else:
            raise Exception("No such robot in this service!")

        service_obj.robots.remove(robot_obj)
        self.robots.append(robot_obj)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service_obj = self.searching_for_service_by_name(service_name)

        [robot.eating() for robot in service_obj.robots]

        return f"Robots fed: {len(service_obj.robots)}."

    def service_price(self, service_name: str):
        service_obj = self.searching_for_service_by_name(service_name)

        total_price = sum([robot.price for robot in service_obj.robots])

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        return "\n".join([service.details() for service in self.services])

    # HELPERS -------------------------------------------------------------------------

    def searching_for_robot_by_name(self, name):
        for robot in self.robots:
            if robot.name == name:
                return robot

    def searching_for_service_by_name(self, name):
        for service in self.services:
            if service.name == name:
                return service
