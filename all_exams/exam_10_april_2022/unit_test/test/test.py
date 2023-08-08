from oop.all_exams.exam_10_april_2022.unit_test.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):

    def setUp(self) -> None:
        self.movie_1 = Movie("Harry Potter and the Sorcerer's Bug", 2023, 9.7)
        self.movie_2 = Movie("Harry Potter and the Order of the Infinite Loops", 2022, 8.9)
        self.movie_3 = Movie("Harry Potter and the Goblet of Errors", 2021, 9.7)
        self.movie_4 = Movie("Short name", 2021, 9.7)
        # I hope someday someone will laugh at this :]

    def test_entry_data(self):
        self.assertEqual("Harry Potter and the Sorcerer's Bug", self.movie_1.name)
        self.assertEqual(2023, self.movie_1.year)
        self.assertEqual(9.7, self.movie_1.rating)

    def test_empty_name(self):
        with self.assertRaises(ValueError) as error:
            self.movie_1.name = ""
        self.assertEqual('Name cannot be an empty string!', str(error.exception))

    def test_year_lower_than_1887(self):
        with self.assertRaises(ValueError) as error:
            self.movie_1.year = 1886
        self.assertEqual("Year is not valid!", str(error.exception))

    def test_add_actor_first_time(self):
        self.movie_1.add_actor("Devihem")
        self.assertEqual(['Devihem'], self.movie_1.actors)

    def test_add_actor_same_twice(self):
        self.movie_1.add_actor("Devihem")
        result = self.movie_1.add_actor("Devihem")
        self.assertEqual("Devihem is already added in the list of actors!", result)

    def test_gt_method_1_greater(self):
        result = self.movie_1 > self.movie_2
        self.assertEqual('''"Harry Potter and the Sorcerer's Bug" is better than '''
                         '''"Harry Potter and the Order of the Infinite Loops"''', result)

    def test_gt_method_1_lower_and_equal(self):
        result = self.movie_2 > self.movie_1
        self.assertEqual('''"Harry Potter and the Sorcerer's Bug" is better than '''
                         '''"Harry Potter and the Order of the Infinite Loops"''', result)

    def test_repr_actors(self):
        self.movie_4.add_actor("Devihem")
        self.movie_4.add_actor("Doffy")
        result = str(self.movie_4)
        self.assertEqual('Name: Short name\nYear of Release: 2021\nRating: 9.70\nCast: Devihem, Doffy', result)


if __name__ == '__main__':
    main()
