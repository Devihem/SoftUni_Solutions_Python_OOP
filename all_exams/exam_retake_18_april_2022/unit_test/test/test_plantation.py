from oop.all_exams.exam_retake_18_april_2022.unit_test.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):

    def setUp(self) -> None:
        self.plantation = Plantation(10)
        self.plantation_test = Plantation(10)
        self.plantation_test.hire_worker("Worker1")
        self.plantation_test.hire_worker("Worker2")
        self.plantation_test.planting("Worker1", "Chicken")
        self.plantation_test.planting("Worker1", "Chicken")
        self.plantation_test.planting("Worker1", "Plant1")
        self.plantation_test.planting("Worker1", "Plant1")

    def test_empty_new_object(self):
        self.assertEqual(10, self.plantation_test.size)

    def test_empty_new_object_2(self):
        self.assertEqual({'Worker1': ['Chicken', 'Chicken', 'Plant1', 'Plant1']}, self.plantation_test.plants)

    def test_empty_new_object3(self):
        self.assertEqual(['Worker1', 'Worker2'], self.plantation_test.workers)

    def test_size_with_lower_value_under_zero(self):
        with self.assertRaises(ValueError) as error:
            Plantation(-1)
        self.assertEqual("Size must be positive number!", str(error.exception))

    def test_hire_worker_correct(self):
        result = self.plantation.hire_worker("Worker1")
        self.assertEqual('Worker1 successfully hired.', result)
        self.assertEqual(['Worker1'], self.plantation.workers)

    def test_hire_worker_already_in_the_list(self):
        with self.assertRaises(ValueError) as error:
            self.plantation_test.hire_worker("Worker1")
        self.assertEqual('Worker already hired!', str(error.exception))

    def test_planting_correct_for_first_time(self):
        result = self.plantation_test.planting("Worker2", "First_Chicken")
        self.assertEqual("Worker2 planted it's first First_Chicken.", result)
        self.assertEqual({'Worker1': ['Chicken', 'Chicken', 'Plant1', 'Plant1'], 'Worker2': ['First_Chicken']},
                         self.plantation_test.plants)

    def test_planting_correct_for_second_time(self):
        result = self.plantation_test.planting("Worker1", "Another_Chicken")
        self.assertEqual('Worker1 planted Another_Chicken.', result)

    def test_planting_plantation_is_already_full(self):
        new_plantation = Plantation(2)
        new_plantation.hire_worker("Worker1")
        new_plantation.planting("Worker1", 'GreeStuff')
        new_plantation.planting("Worker1", 'GreeStuff')
        with self.assertRaises(ValueError) as error:
            new_plantation.planting("Worker1", 'GreeStuff')
        self.assertEqual('The plantation is full!', str(error.exception))

    def test_planting_plantation_with_not_hired_worker(self):
        new_plantation = Plantation(2)
        with self.assertRaises(ValueError) as error:
            new_plantation.planting("Worker1", 'GreeStuff')
        self.assertEqual('Worker with name Worker1 is not hired!', str(error.exception))

    def test_len_dunder_calculation(self):
        self.assertEqual(4, self.plantation_test.__len__())
        self.plantation_test.planting("Worker2", "Something")
        self.assertEqual(5, self.plantation_test.__len__())

    def test_len_dunder_calculation_2(self):
        self.assertEqual(0, self.plantation.__len__())

    def test_repr_dunder_printing(self):
        result = self.plantation_test.__repr__()
        self.assertEqual('Size: 10\nWorkers: Worker1, Worker2',
                         result)

    def test_repr_dunder_printing_2(self):
        self.assertEqual('Plantation size: 10\n', str(self.plantation))
        self.plantation.hire_worker('Worker_1')
        self.plantation.hire_worker('Worker_2')
        self.plantation.planting("Worker_1", "GreenStuff_add")
        self.assertEqual('Size: 10\nWorkers: Worker_1, Worker_2', self.plantation.__repr__())


if __name__ == "__main__":
    main()
