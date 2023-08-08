from oop.all_exams.exam_retake_19_december_2022.unit_test.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):
    def setUp(self) -> None:
        self.driver_1 = TruckDriver("D_Name_1", 5.05)
        self.driver_2 = TruckDriver("D_Name_2", 15.07)
        self.driver_2.available_cargos = {"Bulgaria": 100, "Canada": 3000}
        self.driver_2.earned_money = 10000

    def test_empty_entry_data(self):
        self.assertEqual("D_Name_1", self.driver_1.name)
        self.assertEqual(5.05, self.driver_1.money_per_mile)
        self.assertEqual({}, self.driver_1.available_cargos)
        self.assertEqual(0, self.driver_1.earned_money)
        self.assertEqual(0, self.driver_1.miles)

    def test_props_earned_money_for_negative_money(self):
        with self.assertRaises(ValueError) as error:
            self.driver_1.earned_money = -0.01
        self.assertEqual("D_Name_1 went bankrupt.", str(error.exception))

    def test_props_earned_money_calculating_proper(self):
        self.driver_1.earned_money += 1
        self.assertEqual(1, self.driver_1.earned_money)
        self.driver_1.earned_money += 2
        self.assertEqual(3, self.driver_1.earned_money)
        self.driver_1.earned_money -= 3
        self.assertEqual(0, self.driver_1.earned_money)

    def test_add_cargo_offer_exception(self):
        with self.assertRaises(Exception) as error:
            self.driver_2.add_cargo_offer("Canada", 10)
        self.assertEqual("Cargo offer is already added.", str(error.exception))

    def test_add_cargo_offer_correct(self):
        self.assertEqual({}, self.driver_1.available_cargos)
        result1 = self.driver_1.add_cargo_offer("Varna", 300)
        result2 = self.driver_1.add_cargo_offer("Sofia", 400)
        self.assertEqual({'Sofia': 400, 'Varna': 300}, self.driver_1.available_cargos)
        self.assertEqual("Cargo for 300 to Varna was added as an offer.",result1)
        self.assertEqual("Cargo for 400 to Sofia was added as an offer.",result2)

    def test_eat(self):
        self.assertEqual(10000, self.driver_2.earned_money)
        self.driver_2.eat(2500)
        self.driver_2.eat(500)
        self.driver_2.eat(501)
        self.assertEqual(9960, self.driver_2.earned_money)

    def test_sleep(self):
        self.assertEqual(10000, self.driver_2.earned_money)
        self.driver_2.sleep(3000)
        self.driver_2.sleep(5000)
        self.driver_2.sleep(5010)
        self.assertEqual(9910, self.driver_2.earned_money)

    def test_pump_gas(self):
        self.assertEqual(10000, self.driver_2.earned_money)
        self.driver_2.pump_gas(3000)
        self.driver_2.pump_gas(5000)
        self.driver_2.pump_gas(15000)
        self.assertEqual(9000, self.driver_2.earned_money)

    def test_repair_truck(self):
        self.driver_2.earned_money = 100000
        self.assertEqual(100000, self.driver_2.earned_money)
        self.driver_2.repair_truck(10001)
        self.driver_2.repair_truck(50000)
        self.driver_2.repair_truck(20000)
        self.assertEqual(85000, self.driver_2.earned_money)

    def test_check_for_activities_14000_miles(self):
        self.driver_2.earned_money = 100000
        self.assertEqual(100000, self.driver_2.earned_money)
        self.driver_2.check_for_activities(14000)
        self.assertEqual(86250, self.driver_2.earned_money)

    def test_check_for_activities_0_miles(self):
        self.driver_2.earned_money = 100000
        self.assertEqual(100000, self.driver_2.earned_money)
        self.driver_2.check_for_activities(0)
        self.assertEqual(100000, self.driver_2.earned_money)

    def test_check_for_activities_under_zero_miles(self):
        self.driver_2.earned_money = 100000
        self.assertEqual(100000, self.driver_2.earned_money)
        self.driver_2.check_for_activities(-100)
        self.assertEqual(100000, self.driver_2.earned_money)

    def test_drive_best_cargo_1(self):
        self.driver_2.earned_money = 0
        self.assertEqual("D_Name_2", self.driver_2.name)
        self.assertEqual(15.07, self.driver_2.money_per_mile)
        self.assertEqual({'Bulgaria': 100, 'Canada': 3000}, self.driver_2.available_cargos)
        self.assertEqual(0, self.driver_2.earned_money)
        self.assertEqual(0, self.driver_2.miles)

        result = self.driver_2.drive_best_cargo_offer()
        self.assertEqual("D_Name_2 is driving 3000 to Canada.", result)

        self.assertEqual("D_Name_2", self.driver_2.name)
        self.assertEqual(15.07, self.driver_2.money_per_mile)
        self.assertEqual({'Bulgaria': 100, 'Canada': 3000}, self.driver_2.available_cargos)
        self.assertEqual(43835.0, self.driver_2.earned_money)
        self.assertEqual(3000, self.driver_2.miles)

    def test_drive_best_cargo_2(self):
        self.assertEqual("D_Name_1", self.driver_1.name)
        self.assertEqual(5.05, self.driver_1.money_per_mile)
        self.assertEqual({}, self.driver_1.available_cargos)
        self.assertEqual(0, self.driver_1.earned_money)
        self.assertEqual(0, self.driver_1.miles)

        result = self.driver_1.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.",result)

    def test_dunder_repr(self):
        self.driver_2.drive_best_cargo_offer()
        result = self.driver_2.__repr__()
        self.assertEqual("D_Name_2 has 3000 miles behind his back.", result)


if __name__ == "__main__":
    main()
