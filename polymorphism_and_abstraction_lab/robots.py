class Robot:
    sensor_amount = 1

    def __init__(self, name):
        self.name = name


class MedicalRobot(Robot):
    sensor_amount = 6


class ChefRobot(Robot):
    sensor_amount = 4


class WarRobot(Robot):
    sensor_amount = 12


def number_of_robot_sensors(robot):
    return print(robot.__class__.sensor_amount)


basic_robot = Robot('Robo')
da_vinci = MedicalRobot('Da Vinci')
moley = ChefRobot('Moley')
griffin = WarRobot('Griffin')

number_of_robot_sensors(basic_robot)
number_of_robot_sensors(da_vinci)
number_of_robot_sensors(moley)
number_of_robot_sensors(griffin)
