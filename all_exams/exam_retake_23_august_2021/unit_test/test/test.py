from oop.all_exams.exam_retake_23_august_2021.unit_test.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):

    def setUp(self) -> None:
        self.library = Library("Name")
        self.library_1 = Library("Name_1")

    def test_empty_entry_data_name_only(self):
        self.assertEqual('Name_1', self.library_1.name)
        self.assertEqual({}, self.library_1.readers)
        self.assertEqual({}, self.library_1.books_by_authors)

    def test_name_to_be_empty(self):
        with self.assertRaises(ValueError) as error:
            Library('')
        self.assertEqual('Name cannot be empty string!', str(error.exception))

    def test_adding_book_proper(self):
        self.library.add_book("Oda", "One piece")
        self.assertEqual({'Oda': ['One piece']}, self.library.books_by_authors)

    def test_adding_book_proper_with_author_already_exist(self):
        self.library.add_book("Oda", "One piece")
        self.library.add_book("Oda", "Half piece")
        self.assertEqual({'Oda': ['One piece', 'Half piece']}, self.library.books_by_authors)

    def test_adding_book_all_empty(self):
        self.library.add_book("", "")
        self.assertEqual({'': ['']}, self.library.books_by_authors)

    def test_add_reader_proper(self):
        self.library.add_reader("Devihem")
        self.assertEqual({'Devihem': []}, self.library.readers)

    def test_add_same_reader_twice(self):
        self.library.add_reader("Devihem")
        result = self.library.add_reader("Devihem")
        self.assertEqual('Devihem is already registered in the Name library.', result)

    def test_rent_book_proper(self):
        self.library.add_reader("Devihem")
        self.library.add_book("Oda", "One Piece")
        self.library.rent_book('Devihem', 'Oda', 'One Piece')
        self.assertEqual({'Devihem': [{'Oda': 'One Piece'}]}, self.library.readers)
        self.assertEqual({'Oda': []}, self.library.books_by_authors)

    def test_rent_book_no_reader(self):
        self.library.add_reader("Devihem")
        self.library.add_book("Oda", "One Piece")
        result = self.library.rent_book('Zevihem', 'Oda', 'One Piece')
        self.assertEqual('Zevihem is not registered in the Name Library.', result)

    def test_rent_book_no_author(self):
        self.library.add_reader("Devihem")
        self.library.add_book("Oda", "One Piece")
        result = self.library.rent_book('Devihem', 'GOda', 'One Piece')
        self.assertEqual("Name Library does not have any GOda's books.", result)

    def test_rent_book_no_title(self):
        self.library.add_reader("Devihem")
        self.library.add_book("Oda", "One Piece")
        result = self.library.rent_book('Devihem', 'Oda', 'Half Piece')
        self.assertEqual('''Name Library does not have Oda's "Half Piece".''', result)


if __name__ == '__main__':
    main()
