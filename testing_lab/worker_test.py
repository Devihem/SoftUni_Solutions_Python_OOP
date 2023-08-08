from worker import Worker


from unittest import TestCase, main


class WorkerTests(TestCase):
    def test_worker_is_initialized_correctly(self):
        # Arrange / Act
        worker = Worker("Test", 20, 10)
        # Assert
        self.assertEqual('Test', worker.name)
        self.assertEqual(20, worker.salary)
        self.assertEqual(10, worker.energy)

    def test_energy_is_increased_after_rest(self):
        # Arrange
        worker = Worker("Test", 20, 10)

        self.assertEqual(10, worker.energy)
        # Act
        worker.rest()

        # Assert
        self.assertEqual(11, worker.energy)

    def test_worker_work_with_zero_energy(self):
        # Arrange
        worker = Worker("Test", 20, 0)

        # Assert / Act
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_worker_with_negative_energy_raises(self):
        worker = Worker("Test", 20, -1)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_worker_is_payed_after_working(self):
        # Arrange
        worker = Worker("Test", 20, 10)

        self.assertEqual(0, worker.money)

        # Act
        worker.work()

        # Assert
        self.assertEqual(20, worker.money)

        # Act
        worker.work()

        # Assert
        self.assertEqual(40, worker.money)

    def test_if_the_energy_decreased_after_working(self):
        # Arrange
        worker = Worker("Test", 20, 10)

        # Act
        worker.work()

        # Assert
        self.assertEqual(9, worker.energy)

        # Act
        worker.work()

        # Assert
        self.assertEqual(8, worker.energy)

    def test_get_info(self):
        worker = Worker("Test", 20, 10)
        result = worker.get_info()
        expected = "Test has saved 0 money."
        self.assertEqual(expected, result)
        worker.work()
        result = worker.get_info()
        expected = "Test has saved 20 money."
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
