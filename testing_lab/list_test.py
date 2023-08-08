# Trying to be extra lazy ( FAILED ) the script is awful !
from list import IntegerList

from unittest import TestCase, main


class IntegerListTest(TestCase):

    def test_lazy__init__(self):
        only_ints = IntegerList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        mixed = IntegerList("1", 2.2, True, 4.0, 5, 6, 7, 8, 9, 10)
        empty = IntegerList([])
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], only_ints._IntegerList__data)
        self.assertEqual([5, 6, 7, 8, 9, 10], mixed._IntegerList__data)
        self.assertEqual([], empty._IntegerList__data)

    def test_get_data(self):
        mixed = IntegerList("1", 2.2, True, 4.0, 5, 6, 7, 8, 9, 10)
        self.assertEqual([5, 6, 7, 8, 9, 10], mixed.get_data())

    def test_add(self):
        mixed = IntegerList("1", 2.2, True, 4.0, 5, 6, 7, 8, 9, 10)
        mixed.add(11)
        self.assertEqual([5, 6, 7, 8, 9, 10, 11], mixed._IntegerList__data)

    def test_add_other(self):
        mixed = IntegerList("1", 2.2, True, 4.0, 5, 6, 7, 8, 9, 10)
        with self.assertRaises(ValueError) as expc:
            mixed.add("2")
        self.assertEqual("Element is not Integer", str(expc.exception))

    def test_remove(self):
        mixed = IntegerList("1", 2.2, True, 4.0, 5, 6, 7, 8, 9, 10)
        self.assertEqual([5, 6, 7, 8, 9, 10], mixed._IntegerList__data)
        result = mixed.remove_index(5)
        self.assertEqual(10, result)
        self.assertEqual([5, 6, 7, 8, 9], mixed._IntegerList__data)

    def test_remove_with_bad_index(self):
        mixed = IntegerList("1", 2.2, True, 4.0, 5, 6, 7, 8, 9, 10)
        with self.assertRaises(IndexError) as excp:
            mixed.remove_index(6)
        self.assertEqual("Index is out of range", str(excp.exception))

    def test_get_i_was_missing_it_for_hours_test_1(self):
        mixed = IntegerList("1", 2.2, True, 4.0, 5, 6, 7, 8, 9, 10)
        with self.assertRaises(IndexError) as excp:
            mixed.get(6)
        self.assertEqual("Index is out of range", str(excp.exception))

    def test_get_i_was_missing_it_for_hours_test_2(self):
        mixed = IntegerList("1", 2.2, True, 4.0, 5, 6, 7, 8, 9, 10)
        result = mixed.get(5)
        self.assertEqual(10, result)
    def test_insert(self):
        mixed = IntegerList("1", 2.2, True, 4.0, 5, 6, 7, 8, 9, 10)
        mixed.insert(0, 11)
        self.assertEqual([11, 5, 6, 7, 8, 9, 10], mixed._IntegerList__data)

    def test_insert_with_bad_index(self):
        mixed = IntegerList("1", 2.2, True, 4.0, 5, 6, 7, 8, 9, 10)
        with self.assertRaises(IndexError) as excp:
            mixed.insert(6, 11)
        self.assertEqual("Index is out of range", str(excp.exception))

    def test_insert_with_bad_index_2(self):
        mixed = IntegerList("1", 2.2, True, 4.0, 5, 6, 7, 8, 9, 10)
        with self.assertRaises(ValueError) as excp:
            mixed.insert(3, "11")
        self.assertEqual("Element is not Integer", str(excp.exception))

    def test_get_biggest(self):
        mixed = IntegerList("1", 2.2, True, 4.0, 5, 6, 7, 8, 9, 10)
        self.assertEqual(10, mixed.get_biggest())

    def test_index(self):
        mixed = IntegerList("1", 2.2, True, 4.0, 5, 6, 7, 8, 9, 10)
        self.assertEqual(5, mixed.get_index(10))


if __name__ == "__main__":
    main()
