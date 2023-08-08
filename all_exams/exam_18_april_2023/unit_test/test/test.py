from oop.all_exams.exam_16_august_2020.unit_test.project import Robot
from unittest import TestCase, main


class TestRobot(TestCase):
    def setUp(self) -> None:
        self.robot = Robot("12345", "Military", 100, 1000.0)

    def test_entry_data_valid(self):
        self.assertEqual("12345", self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(100, self.robot.available_capacity)
        self.assertEqual(1000.0, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_wrong_category_robot(self):
        with self.assertRaises(ValueError) as error:
            self.robot.category = "Opitimus-Praim"
        self.assertEqual("Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'",
                         str(error.exception))

    def test_wrong_price_robot(self):
        with self.assertRaises(ValueError) as error:
            self.robot.price = -1
        self.assertEqual('Price cannot be negative!', str(error.exception))

    def test_upgrade_with_same_part(self):
        self.robot.hardware_upgrades = ['CPU']
        result = self.robot.upgrade('CPU', 0.0)
        self.assertEqual('Robot 12345 was not upgraded.', result)

    # double price test if needed
    def test_upgrade_with_proper_data(self):
        result = self.robot.upgrade('CPU', 2.2)
        self.assertEqual(1003.3, self.robot.price)
        self.assertEqual(['CPU'], self.robot.hardware_upgrades)
        self.assertEqual('Robot 12345 was upgraded with CPU.', result)

    def test_update_no_capacity(self):
        self.robot.software_updates = [1.0, 2.0, 3.0, 4.0, 5.0]
        result = self.robot.update(5.1, 101)
        self.assertEqual('Robot 12345 was not updated.', result)

    def test_update_lower_or_same_version(self):
        self.robot.software_updates = [1.0, 2.0, 3.0, 4.0, 5.0]
        result = self.robot.update(5, 10)
        self.assertEqual('Robot 12345 was not updated.', result)

    def test_update_higher_version(self):
        self.robot.software_updates = [1.0, 2.0, 3.0, 4.0, 5.0]
        result = self.robot.update(7, 10)
        self.assertEqual('Robot 12345 was updated to version 7.', result)

    def test_gt_method_for_equal_price(self):
        robot_new = Robot("12345", "Military", 100, 1000.0)
        result = self.robot > robot_new
        self.assertEqual('Robot with ID 12345 costs equal to Robot with ID 12345.', result)

    def test_gt_method_for_greater(self):
        robot_new = Robot("12345", "Military", 100, 999)
        result = self.robot > robot_new
        self.assertEqual('Robot with ID 12345 is more expensive than Robot with ID 12345.', result)

    def test_gt_method_for_lower_than(self):
        robot_new = Robot("12345", "Military", 100, 1001.0)
        result = self.robot > robot_new
        self.assertEqual('Robot with ID 12345 is cheaper than Robot with ID 12345.', result)


# GT - Greater Than


if __name__ == "__main__":
    main()
