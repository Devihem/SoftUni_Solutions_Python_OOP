from unittest import TestCase, main
from oop.all_exams.exam_16_august_2020.unit_test.project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):

    def setUp(self) -> None:
        self.factory_1 = PaintFactory("Big_Factory", 100)

    def test_entry_data(self):
        self.assertEqual('Big_Factory', self.factory_1.name)
        self.assertEqual(100, self.factory_1.capacity)
        self.factory_1.add_ingredient('red', 50)
        result = self.factory_1.products
        self.assertEqual({'red': 50}, result)

    def test_add_ingredient_correct_red_50_and_more_red_50(self):
        self.factory_1.add_ingredient('red', 50)
        self.assertEqual({'red': 50}, self.factory_1.ingredients)
        self.factory_1.add_ingredient('red', 50)
        self.assertEqual({'red': 100}, self.factory_1.ingredients)

    def test_add_ingredient_over_capacity_red_101(self):
        with self.assertRaises(ValueError) as error:
            self.factory_1.add_ingredient('red', 101)
        self.assertEqual('Not enough space in factory', str(error.exception))

    def test_add_ingredient_not_allowed_brown_100(self):
        with self.assertRaises(TypeError) as error:
            self.factory_1.add_ingredient('brown', 100)
        self.assertEqual('Ingredient of type brown not allowed in PaintFactory', str(error.exception))

    def test_remove_ingredient_correct_red_100(self):
        self.factory_1.add_ingredient('red', 100)
        self.factory_1.remove_ingredient('red', 99)
        self.assertEqual({'red': 1}, self.factory_1.ingredients)

    def test_remove_ingredient_incorrect_red_101(self):
        self.factory_1.add_ingredient('red', 100)
        with self.assertRaises(ValueError) as error:
            self.factory_1.remove_ingredient('red', 101)
        self.assertEqual('Ingredients quantity cannot be less than zero', str(error.exception))

    # KeyError add extra quotes  - who to know
    def test_remove_ingredient_not_in_list_ded_99(self):
        self.factory_1.add_ingredient('red', 100)
        with self.assertRaises(KeyError) as error:
            self.factory_1.remove_ingredient('ded', 99)
        self.assertEqual("'No such ingredient in the factory'", str(error.exception))

    def test_repr_method(self):
        self.factory_1.add_ingredient('red', 100)
        result = str(self.factory_1)
        self.assertEqual('Factory name: Big_Factory with capacity 100.\nred: 100\n', result)


if __name__ == '__main__':
    main()
