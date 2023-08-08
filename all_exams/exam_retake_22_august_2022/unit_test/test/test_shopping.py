from oop.all_exams.exam_retake_22_august_2022.unit_test.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):

    def setUp(self) -> None:
        self.empty_shop = ShoppingCart("ShopEmpty", 100.2)
        self.remove_shop = ShoppingCart("ShopRemove", 100.2)
        self.add_shop = ShoppingCart("AddShop", 1220.2)
        self.add_shop.add_to_cart("Banana", 10.34)
        self.add_shop.add_to_cart("Zebra", 50.322)
        self.remove_shop.add_to_cart("Banana", 27.34)
        self.remove_shop.add_to_cart("Banana", 37.34)
        self.remove_shop.add_to_cart("RedBull", 99.99999999999)
        self.new_shop = self.remove_shop.__add__(self.add_shop)

    def test_entry_data(self):
        self.assertEqual(100.2, self.empty_shop.budget)
        self.assertEqual("ShopEmpty", self.empty_shop.shop_name)
        self.assertEqual({}, self.empty_shop.products)

    def test_shop_name_getter_no_capital(self):
        with self.assertRaises(ValueError) as error:
            ShoppingCart("shop", 10)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(error.exception))

    def test_shop_name_getter_no_only_alpha(self):
        with self.assertRaises(ValueError) as error:
            ShoppingCart("Shop1", 10)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(error.exception))

    def test_shop_name_getter_space_in_name(self):
        with self.assertRaises(ValueError) as error:
            ShoppingCart("Shop Goodies", 10)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(error.exception))

    def test_add_to_cart(self):
        result1 = self.empty_shop.add_to_cart("Banana", 27.34)
        self.assertEqual({'Banana': 27.34}, self.empty_shop.products)
        result2 = self.empty_shop.add_to_cart("Banana", 37.34)
        result3 = self.empty_shop.add_to_cart("RedBull", 99.99999999999)
        self.assertEqual("Banana product was successfully added to the cart!", result1)
        self.assertEqual("Banana product was successfully added to the cart!", result2)
        self.assertEqual("RedBull product was successfully added to the cart!", result3)
        self.assertEqual({'Banana': 37.34, 'RedBull': 99.99999999999}, self.empty_shop.products)

    def test_add_to_cart_to_expensive_product_1(self):
        with self.assertRaises(ValueError) as error:
            self.empty_shop.add_to_cart("Gift", 100)
        self.assertEqual("Product Gift cost too much!", str(error.exception))

    def test_add_to_cart_to_expensive_product_2(self):
        with self.assertRaises(ValueError) as error:
            self.empty_shop.add_to_cart("Gift", 200)
        self.assertEqual("Product Gift cost too much!", str(error.exception))

    def test_remove_product_value_error_no_such_product(self):
        with self.assertRaises(ValueError) as error:
            self.empty_shop.remove_from_cart("Banana")
        self.assertEqual("No product with name Banana in the cart!", str(error.exception))

    def test_remove_product_value_error_remove_something_twice(self):
        with self.assertRaises(ValueError) as error:
            self.remove_shop.remove_from_cart("RedBull")
            self.remove_shop.remove_from_cart("RedBull")
        self.assertEqual("No product with name RedBull in the cart!", str(error.exception))

    def test_remove_product_correct(self):
        self.assertEqual({'Banana': 37.34, 'RedBull': 99.99999999999}, self.remove_shop.products)
        result1 = self.remove_shop.remove_from_cart("RedBull")
        self.assertEqual({'Banana': 37.34}, self.remove_shop.products)
        self.assertEqual("Product RedBull was successfully removed from the cart!", result1)
        result2 = self.remove_shop.remove_from_cart("Banana")
        self.assertEqual("Product Banana was successfully removed from the cart!", result2)
        self.assertEqual({}, self.remove_shop.products)

    def test_dunder_add_1(self):
        new_shop = self.remove_shop.__add__(self.add_shop)
        self.assertEqual("ShopRemoveAddShop", new_shop.shop_name)
        self.assertEqual(1320.4, new_shop.budget)
        self.assertEqual({'Banana': 10.34, 'RedBull': 99.99999999999, 'Zebra': 50.322}, new_shop.products)

    def test_buy_product_1(self):
        result1 = self.empty_shop.buy_products()
        result3 = self.new_shop.buy_products()
        self.assertEqual("Products were successfully bought! Total cost: 0.00lv.", result1)
        self.assertEqual("Products were successfully bought! Total cost: 160.66lv.", result3)

    def test_buy_product_value_error(self):
        with self.assertRaises(ValueError) as error:
            self.remove_shop.buy_products()
        self.assertEqual("Not enough money to buy the products! Over budget with 37.14lv!", str(error.exception))


if __name__ == "__main__":
    main()
