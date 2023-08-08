from vehicle import Vehicle
from unittest import TestCase


class TestVehicle(TestCase):
    def test_entry_data(self):
        car = Vehicle(100, 100)
        self.assertEqual(100, car.fuel)
        self.assertEqual(100, car.capacity)
        self.assertEqual(100, car.horse_power)
        self.assertEqual(1.25, car.fuel_consumption)

    def test_drive(self):
        car = Vehicle(100, 100)
        car.drive(10)
        self.assertEqual(87.5, car.fuel)

    def test_drive_exception(self):
        car = Vehicle(100, 100)
        with self.assertRaises(Exception) as error:
            car.drive(100)
        self.assertEqual("Not enough fuel", str(error.exception))

    def test_refuel_normal(self):
        car = Vehicle(100, 100)
        car.fuel = 99
        car.refuel(1)
        self.assertEqual(100, car.fuel)

    def test_refuel_exception(self):
        car = Vehicle(100, 100)
        with self.assertRaises(Exception) as error:
            car.refuel(1)
        self.assertEqual("Too much fuel", str(error.exception))

    def test_string_print(self):
        car = Vehicle(100, 100)
        result = str(car)
        self.assertEqual('The vehicle has 100 horse power with 100 fuel left and 1.25 fuel consumption', str(car))


if __name__ == "__main__":
    main()
