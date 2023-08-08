from mammal import Mammal
from unittest import TestCase


class TestMammal(TestCase):
    def test_entry_data(self):
        animal = Mammal("Max", "Dog", "Meow")
        self.assertEqual("Max", animal.name)
        self.assertEqual("Dog", animal.type)
        self.assertEqual("Meow", animal.sound)

    def test_sound(self):
        animal = Mammal("Max", "Dog", "Meow")
        result = animal.make_sound()
        self.assertEqual('Max makes Meow', result)

    def test_get_kingdom(self):
        animal = Mammal("Max", "Dog", "Meow")
        result = animal.get_kingdom()
        self.assertEqual('animals', result)

    def test_print_info(self):
        animal = Mammal("Max", "Dog", "Meow")
        result = animal.info()
        self.assertEqual('Max is of type Dog', result)


if __name__ == "__main__":
    main()
