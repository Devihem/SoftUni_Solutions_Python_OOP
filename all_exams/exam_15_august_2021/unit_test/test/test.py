from oop.all_exams.exam_15_august_2021.unit_test.pet_shop import PetShop
from unittest import TestCase, main


class TestPetShop(TestCase):

    def setUp(self) -> None:
        self.petshop_1 = PetShop("寵物店煮熟的狗")
        self.petshop_1.food = {"Meat": 10, "Fish": 10}
        self.petshop_1.pets = ['Dog_1', 'Dog_2']

    def test_pet_shop_initialization_with_empty(self):
        self.pet_shop = PetShop("My Pet Shop")
        self.assertEqual(self.pet_shop.name, "My Pet Shop")
        self.assertEqual(self.pet_shop.food, {})
        self.assertEqual(self.pet_shop.pets, [])

    def test_entry_data(self):
        self.assertEqual('寵物店煮熟的狗', self.petshop_1.name)
        self.assertEqual({'Fish': 10, 'Meat': 10}, self.petshop_1.food)
        self.assertEqual(['Dog_1', 'Dog_2'], self.petshop_1.pets)

    def test_add_food_correct(self):
        result = self.petshop_1.add_food("Bones ?", 10)
        self.assertEqual('Successfully added 10.00 grams of Bones ?.', result)
        self.petshop_1.add_food("Bones ?", 10)
        self.assertEqual({'Bones ?': 20, 'Fish': 10, 'Meat': 10}, self.petshop_1.food)

    def test_add_under_zero_food(self):
        with self.assertRaises(ValueError) as error:
            self.petshop_1.add_food("Bones ?", -10)
        self.assertEqual("Quantity cannot be equal to or less than 0", str(error.exception))

    def test_add_exactly_zero_food(self):
        with self.assertRaises(ValueError) as error:
            self.petshop_1.add_food("Bones ?", 0)
        self.assertEqual("Quantity cannot be equal to or less than 0", str(error.exception))

    def test_add_pet_correct(self):
        result = self.petshop_1.add_pet("Cat_1")
        self.assertEqual(['Dog_1', 'Dog_2', 'Cat_1'], self.petshop_1.pets)
        self.assertEqual("Successfully added Cat_1.", result)

    def test_add_pet_double_name(self):
        with self.assertRaises(Exception) as error:
            self.petshop_1.add_pet("Dog_5")
            self.petshop_1.add_pet("Dog_5")
        self.assertEqual(['Dog_1', 'Dog_2', 'Dog_5'],self.petshop_1.pets)
        self.assertEqual("Cannot add a pet with the same name", str(error.exception))

    def test_feed_pet_correct(self):
        self.petshop_1.add_food("Meat", 1000)
        result = self.petshop_1.feed_pet("Meat", "Dog_1")
        self.assertEqual('Dog_1 was successfully fed', result)
        self.assertEqual({'Fish': 10, 'Meat': 910}, self.petshop_1.food)

    def test_feed_pet_without_food(self):
        result = self.petshop_1.feed_pet("Meat", "Dog_1")
        self.assertEqual('Adding food...', result)
        self.assertEqual({'Fish': 10, 'Meat': 1010.0}, self.petshop_1.food)

    def test_feed_pet_without_this_type_of_food_in_dict(self):
        result = self.petshop_1.feed_pet("Zebra", "Dog_1")
        self.assertEqual('You do not have Zebra', result)

    def test_feed_pet_with_wrong_name_pet(self):
        with self.assertRaises(Exception) as error:
            self.petshop_1.feed_pet("python_code", "TheLegendaryBug")
        self.assertEqual('Please insert a valid pet name', str(error.exception))

    def test_repr_method(self):
        result = str(self.petshop_1)
        self.assertEqual('Shop 寵物店煮熟的狗:\nPets: Dog_1, Dog_2', result)


if __name__ == "__main__":
    main()
