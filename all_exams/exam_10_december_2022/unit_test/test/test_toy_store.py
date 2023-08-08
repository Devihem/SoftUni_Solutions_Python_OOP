from oop.all_exams.exam_10_december_2022.unit_test.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):

    def setUp(self) -> None:
        self.empty_store = ToyStore()
        self.toy_store = ToyStore()
        self.toy_store.toy_shelf = {
            "A": "Luffy",
            "B": "Naruto",
            "C": "Goku",
            "D": "Ueki",
            "E": "Ichigo",
            "F": None,
            "G": None,
        }

    def test_empty_store_data(self):
        self.assertEqual({'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
                         self.empty_store.toy_shelf)

    def test_add_toy_missing_shelf(self):
        with self.assertRaises(Exception) as error:
            self.empty_store.add_toy("A1", "Tiger")
        self.assertEqual("Shelf doesn't exist!", str(error.exception))

    def test_add_toy_already_existing(self):
        with self.assertRaises(Exception) as error:
            self.toy_store.add_toy("A", "Luffy")
        self.assertEqual("Toy is already in shelf!", str(error.exception))

    def test_add_toy_shelf_is_taken(self):
        with self.assertRaises(Exception) as error:
            self.toy_store.add_toy("B", "Luffy")
        self.assertEqual("Shelf is already taken!", str(error.exception))

    def test_add_toy_correct_1(self):
        result = self.toy_store.add_toy("F", "Villain with glasses")
        self.assertEqual("Toy:Villain with glasses placed successfully!", result)
        self.assertEqual(
            {'A': 'Luffy', 'B': 'Naruto', 'C': 'Goku', 'D': 'Ueki', 'E': 'Ichigo', 'F': 'Villain with glasses',
             'G': None}, self.toy_store.toy_shelf)

    def test_remove_toy_not_existing_shelf(self):
        with self.assertRaises(Exception) as error:
            self.toy_store.remove_toy("A1", "Luffy")
        self.assertEqual("Shelf doesn't exist!", str(error.exception))

    def test_remove_toy(self):
        with self.assertRaises(Exception) as error:
            self.toy_store.remove_toy("B", "Luffy")
        self.assertEqual("Toy in that shelf doesn't exists!", str(error.exception))

    def test_remove_toy_correct_1(self):
        result = self.toy_store.remove_toy("A", "Luffy")
        self.assertEqual("Remove toy:Luffy successfully!", result)
        self.assertEqual(
            {'A': None, 'B': 'Naruto', 'C': 'Goku', 'D': 'Ueki', 'E': 'Ichigo', 'F': None,
             'G': None}, self.toy_store.toy_shelf)


if __name__ == "__main__":
    main()
