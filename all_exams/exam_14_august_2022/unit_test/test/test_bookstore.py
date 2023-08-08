from oop.all_exams.exam_14_august_2022.unit_test.bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):
    def setUp(self) -> None:
        self.bookstore_1 = Bookstore(10)
        self.bookstore_2 = Bookstore(10)
        self.bookstore_2.availability_in_store_by_book_titles = {"Book1": 5, "Book2": 2}

    def test_protected_method_total_sold_books(self):
        self.assertEqual(self.bookstore_1.total_sold_books, self.bookstore_1._Bookstore__total_sold_books)

    def test_check_empty_bookstore(self):
        self.assertEqual(({}), self.bookstore_1.availability_in_store_by_book_titles)
        self.assertEqual(10, self.bookstore_1.books_limit)
        self.assertEqual(0, self.bookstore_1.total_sold_books)

    def test_book_limit_zero(self):
        with self.assertRaises(ValueError) as error:
            Bookstore(0)
        self.assertEqual('Books limit of 0 is not valid', str(error.exception))

    def test_book_limit_under_zero(self):
        with self.assertRaises(ValueError) as error:
            Bookstore(-10)
        self.assertEqual('Books limit of -10 is not valid', str(error.exception))

    def test_dunder_len_zero(self):
        self.assertEqual(0, self.bookstore_1.__len__())

    def test_dunder_len_five_and_two_count(self):
        self.assertEqual(7, self.bookstore_2.__len__())

    def test_receive_book_correct_add_twice_same_book(self):
        result1 = self.bookstore_1.receive_book('Book3', 5)
        self.assertEqual(5, self.bookstore_1.__len__())
        self.assertEqual({'Book3': 5}, self.bookstore_1.availability_in_store_by_book_titles)

        result2 = self.bookstore_1.receive_book('Book3', 4)
        self.assertEqual(9, self.bookstore_1.__len__())
        self.assertEqual({'Book3': 9}, self.bookstore_1.availability_in_store_by_book_titles)

        result3 = self.bookstore_1.receive_book('Book5', 1)
        self.assertEqual({'Book3': 9, 'Book5': 1}, self.bookstore_1.availability_in_store_by_book_titles)

        self.assertEqual('5 copies of Book3 are available in the bookstore.', result1)
        self.assertEqual('9 copies of Book3 are available in the bookstore.', result2)
        self.assertEqual('1 copies of Book5 are available in the bookstore.', result3)

    def test_receive_book_to_much_books(self):
        with self.assertRaises(Exception) as error:
            self.bookstore_1.receive_book("Book4", 11)
        self.assertEqual('Books limit is reached. Cannot receive more books!', str(error.exception))

    def test_sell_books_proper(self):
        result = self.bookstore_2.sell_book("Book1", 1)
        result2 = self.bookstore_2.sell_book("Book1", 2)
        self.assertEqual("Sold 1 copies of Book1", result)
        self.assertEqual("Sold 2 copies of Book1", result2)
        self.assertEqual(3, self.bookstore_2.total_sold_books)
        self.assertEqual({'Book1': 2, 'Book2': 2}, self.bookstore_2.availability_in_store_by_book_titles)
        self.assertEqual(4, len(self.bookstore_2))
        result3 = self.bookstore_2.sell_book("Book2", 2)
        self.assertEqual("Sold 2 copies of Book2", result3)
        self.assertEqual({'Book1': 2, 'Book2': 0}, self.bookstore_2.availability_in_store_by_book_titles)

    def test_sell_books_to_much_books_exception(self):
        with self.assertRaises(Exception) as error:
            self.bookstore_2.sell_book("Book1", 6)
        self.assertEqual('Book1 has not enough copies to sell. Left: 5', str(error.exception))

    def test_sell_books_no_such_book_in_store(self):
        with self.assertRaises(Exception) as error:
            self.bookstore_2.sell_book("Book 69", 6)
        self.assertEqual("Book Book 69 doesn't exist!", str(error.exception))

    def test_dunder_str(self):
        self.bookstore_2.sell_book("Book1", 1)
        self.bookstore_2.sell_book("Book1", 2)
        result = self.bookstore_2.__str__()

        self.assertEqual('Total sold books: 3\nCurrent availability: 4\n - Book1: 2 copies\n - Book2: 2 copies', result)


if __name__ == "__main__":
    main()
