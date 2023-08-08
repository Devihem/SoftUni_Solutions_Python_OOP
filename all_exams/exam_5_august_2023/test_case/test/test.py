from oop.all_exams.exam_5_august_2023.test_case.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):
    def setUp(self) -> None:
        self.car_1 = SecondHandCar("Name1", "Type1", 100_000, 123.456)
        self.car_2 = SecondHandCar("Name2", "Type1", 100_000, 123.456)
        self.car_3 = SecondHandCar("Name3", "Type1", 100_000, 121.456)
        self.car_4 = SecondHandCar("Name4", "Type1", 100_000, 126.453)
        self.car_5 = SecondHandCar("Name4", "Type2", 100_000, 126.456)
        self.car_5.repairs = ['Repair1', 'Repair2', 'Repair3', 'Repair4']

    def test_empty_input_base(self):
        self.assertEqual("Name1", self.car_1.model)
        self.assertEqual("Type1", self.car_1.car_type)
        self.assertEqual(100000, self.car_1.mileage)
        self.assertEqual(123.456, self.car_1.price)
        self.assertEqual([], self.car_1.repairs)

    def test_price_props_1(self):
        with self.assertRaises(ValueError) as error:
            SecondHandCar("Name0", "Type0", 100_000, 1)
        self.assertEqual("Price should be greater than 1.0!", str(error.exception))

    def test_price_props_2(self):
        with self.assertRaises(ValueError) as error:
            SecondHandCar("Name0", "Type0", 100_000, 1.0)
        self.assertEqual("Price should be greater than 1.0!", str(error.exception))

    def test_price_props_3(self):
        with self.assertRaises(ValueError) as error:
            SecondHandCar("Name0", "Type0", 100_000, 0.9999999)
        self.assertEqual("Price should be greater than 1.0!", str(error.exception))

    def test_price_props_4(self):
        with self.assertRaises(ValueError) as error:
            SecondHandCar("Name0", "Type0", 100_000, 0)
        self.assertEqual("Price should be greater than 1.0!", str(error.exception))

    def test_price_props_5(self):
        with self.assertRaises(ValueError) as error:
            SecondHandCar("Name0", "Type0", 100_000, -1.1)
        self.assertEqual("Price should be greater than 1.0!", str(error.exception))

    def test_mileage_props_1(self):
        with self.assertRaises(ValueError) as error:
            SecondHandCar("Name0", "Type0", 100, 123.456)
        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(error.exception))

    def test_mileage_props_2(self):
        with self.assertRaises(ValueError) as error:
            SecondHandCar("Name0", "Type0", 99, 123.456)
        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(error.exception))

    def test_mileage_props_3(self):
        with self.assertRaises(ValueError) as error:
            SecondHandCar("Name0", "Type0", 0, 123.456)
        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(error.exception))

    def test_mileage_props_4(self):
        with self.assertRaises(ValueError) as error:
            SecondHandCar("Name0", "Type0", -101, 123.456)
        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(error.exception))

    def test_set_promotional_price_error_1(self):
        with self.assertRaises(ValueError) as error:
            self.car_1.set_promotional_price(123.456)
        self.assertEqual("You are supposed to decrease the price!", str(error.exception))

    def test_set_promotional_price_error_2(self):
        with self.assertRaises(ValueError) as error:
            self.car_1.set_promotional_price(124)
        self.assertEqual("You are supposed to decrease the price!", str(error.exception))

    def test_set_promotional_price_error_3(self):
        with self.assertRaises(ValueError) as error:
            self.car_1.set_promotional_price(-100)
        self.assertEqual("Price should be greater than 1.0!", str(error.exception))

    def test_set_promotional_price_correct_1(self):
        result = self.car_1.set_promotional_price(123.455)
        self.assertEqual("The promotional price has been successfully set.", result)
        self.assertEqual(123.455, self.car_1.price)

    def test_set_promotional_price_correct_2(self):
        result = self.car_1.set_promotional_price(99)
        self.assertEqual("The promotional price has been successfully set.", result)
        self.assertEqual(99, self.car_1.price)

    def test_need_repair_1(self):
        result = self.car_1.need_repair(61.729, "Repair1")
        self.assertEqual("Repair is impossible!", result)
        self.assertEqual([], self.car_1.repairs)

    def test_need_repair_2(self):
        result1 = self.car_1.need_repair(61.728, "Repair1")
        self.assertEqual(['Repair1'], self.car_1.repairs)
        self.assertEqual("Price has been increased due to repair charges.", result1)
        self.assertEqual(185.184, self.car_1.price)

        result2 = self.car_1.need_repair(61.728, "Repair2")
        self.assertEqual("Price has been increased due to repair charges.", result2)
        self.assertEqual(['Repair1', 'Repair2'], self.car_1.repairs)
        self.assertEqual(246.912, self.car_1.price)

        result3 = self.car_1.need_repair(123.457, "Repair3")
        self.assertEqual("Repair is impossible!", result3)
        self.assertEqual(['Repair1', 'Repair2'], self.car_1.repairs)
        self.assertEqual(246.912, self.car_1.price)

    def test_dunder_gt_1(self):
        result = self.car_1.__gt__(self.car_2)
        self.assertEqual(False, result)

    def test_dunder_gt_2(self):
        result = self.car_1.__gt__(self.car_3)
        self.assertEqual(True, result)

    def test_dunder_gt_3(self):
        result = self.car_1.__gt__(self.car_4)
        self.assertEqual(False, result)

    def test_dunder_gt_4(self):
        result = self.car_1.__gt__(self.car_5)
        self.assertEqual("Cars cannot be compared. Type mismatch!", result)

    def test_dunder_str_1(self):
        result = self.car_5.__str__()
        self.assertEqual("Model Name4 | Type Type2 | Milage 100000km\nCurrent price: 126.46 | Number of Repairs: 4",
                         result)

    def test_dunder_str_2(self):
        result = self.car_4.__str__()
        self.assertEqual("Model Name4 | Type Type1 | Milage 100000km\nCurrent price: 126.45 | Number of Repairs: 0",
                         result)


if __name__ == "__main__":
    main()
