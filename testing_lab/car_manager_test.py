from car_manager import Car
from unittest import TestCase, main


class CarTest(TestCase):
    def test_starting_information_all_correct(self):
        # Car (Str, Str, Int, Int)
        car_1 = Car("Audi", "A3", 1, 10)
        self.assertEqual("Audi", car_1.make)
        self.assertEqual("A3", car_1.model)
        self.assertEqual(1, car_1.fuel_consumption)
        self.assertEqual(10, car_1.fuel_capacity)
        self.assertEqual(0, car_1.fuel_amount)

    def test_make_incorrect(self):
        with self.assertRaises(Exception) as excp:
            car_1 = Car("", "A3", 1, 10)
        self.assertEqual("Make cannot be null or empty!", str(excp.exception))

    def test_model_incorrect(self):
        with self.assertRaises(Exception) as excp:
            car_1 = Car("Audi", "", 1, 10)
        self.assertEqual("Model cannot be null or empty!", str(excp.exception))

    def test_fuel_consumption_incorrect(self):
        with self.assertRaises(Exception) as excp:
            car_1 = Car("Audi", "A3", -1, 10)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(excp.exception))

    def test_fuel_capacity_incorrect(self):
        with self.assertRaises(Exception) as excp:
            car_1 = Car("Audi", "A3", 1, -1)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(excp.exception))

    def test_fuel_amount_incorrect(self):
        car_1 = Car("Audi", "A3", 1, 10)
        with self.assertRaises(Exception) as excp:
            car_1.fuel_amount = -2
        self.assertEqual("Fuel amount cannot be negative!", str(excp.exception))

    def test_refuel_correct(self):
        car_1 = Car("Audi", "A3", 1, 10)
        car_1.refuel(5)
        self.assertEqual(5, car_1.fuel_amount)

    def test_refuel_over_the_limit(self):
        car_1 = Car("Audi", "A3", 1, 10)
        car_1.refuel(50)
        self.assertEqual(10, car_1.fuel_amount)

    def test_refuel_incorrect(self):
        car_1 = Car("Audi", "A3", 1, 10)
        with self.assertRaises(Exception) as excp:
            car_1.refuel(-10)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(excp.exception))

    def test_drive_use_all_fuel_correct(self):
        car_1 = Car("Audi", "A3", 1, 10)
        car_1.refuel(10)
        car_1.drive(1000)
        self.assertEqual(0, car_1.fuel_amount)

    def test_drive_distance_to_long(self):
        car_1 = Car("Audi", "A3", 1, 9)
        car_1.refuel(9)
        with self.assertRaises(Exception) as excp:
            car_1.drive(1000)
        self.assertEqual("You don't have enough fuel to drive!", str(excp.exception))


if __name__ == "__main__":
    main()
