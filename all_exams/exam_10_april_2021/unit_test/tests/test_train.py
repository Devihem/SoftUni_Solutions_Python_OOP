from oop.all_exams.exam_10_april_2021.unit_test.project.train.train import Train
from unittest import TestCase, main


class TestTrain(TestCase):
    def setUp(self) -> None:
        self.train_1 = Train("Hogwarts Express", 3)

    def test_entry_data(self):
        self.assertEqual('Hogwarts Express', self.train_1.name)
        self.assertEqual(3, self.train_1.capacity)
        self.assertEqual([], self.train_1.passengers)

    def test_add_proper_data(self):
        self.train_1.add("Name_1")
        self.train_1.add("Name_2")
        result = self.train_1.add("Name_3")
        self.assertEqual(['Name_1', 'Name_2', 'Name_3'], self.train_1.passengers)
        self.assertEqual('Added passenger Name_3', result)

    def test_add_to_much_ppl(self):
        self.train_1.add("Name_1")
        self.train_1.add("Name_2")
        self.train_1.add("Name_3")

        with self.assertRaises(ValueError) as error:
            self.train_1.add("Name_4")
        self.assertEqual('Train is full', str(error.exception))

    def test_add_the_same_name(self):
        self.train_1.add("Name_1")
        self.train_1.add("Name_2")

        with self.assertRaises(ValueError) as error:
            self.train_1.add("Name_2")
        self.assertEqual('Passenger Name_2 Exists', str(error.exception))

    def test_remove_proper(self):
        self.train_1.add("Name_1")
        result = self.train_1.remove("Name_1")
        self.assertEqual('Removed Name_1', result)

    def test_removed_missing_name(self):
        with self.assertRaises(ValueError) as error:
            self.train_1.remove("Name_1")
        self.assertEqual('Passenger Not Found', str(error.exception))


if __name__ == "__main__":
    main()
