from cat import Cat
from unittest import TestCase, main


class CatTest(TestCase):
    def test_cat_size_increase_after_eating(self):
        # Arrange
        cat = Cat("Nekomamushi")

        # Base_Asset
        self.assertEqual(0, cat.size)

        # Act
        cat.eat()

        # Asset
        self.assertEqual(1, cat.size)

    def test_cat_is_fed_after_eating(self):
        # Arrange
        cat = Cat("Nekomamushi")
        cat.eat()
        self.assertTrue(cat.fed)

    def test_cat_is_fed_after_eating_raise_error(self):
        # Arrange
        cat = Cat("Nekomamushi")
        cat.eat()
        self.assertTrue(cat.fed)

        with self.assertRaises(Exception) as excp:
            cat.eat()
        self.assertEqual('Already fed.', str(excp.exception))

    def test_cat_cannot_go_to_sleep_without_food_raise_error(self):
        # Arrange
        cat = Cat("Nekomamushi")

        with self.assertRaises(Exception) as excp:
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(excp.exception))

    def test_cat_is_not_sleepy_after_sleep(self):
        cat = Cat("Nekomamushi")
        cat.eat()
        cat.sleep()

        self.assertFalse(cat.sleepy)


if __name__ == "__main__":
    main()
