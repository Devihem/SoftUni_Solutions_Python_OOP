from oop.all_exams.exam_retake_22_august_2022.structure_and_func.client import Client
from oop.all_exams.exam_retake_22_august_2022.structure_and_func.meals.main_dish import MainDish
from oop.all_exams.exam_retake_22_august_2022.structure_and_func.meals.dessert import Dessert
from oop.all_exams.exam_retake_22_august_2022.structure_and_func.meals.starter import Starter


class FoodOrdersApp:
    def __init__(self):
        self.menu = []
        self.clients_list = []
        self.receipt_id = 0

    def register_client(self, client_phone_number: str):
        if self.search_for_client(client_phone_number):
            raise Exception("The client has already been registered!")

        created_client = Client(client_phone_number)
        self.clients_list.append(created_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals_obj):
        for meal in meals_obj:
            if isinstance(meal, (Starter, MainDish, Dessert)):
                self.menu.append(meal)

    def show_menu(self):
        self.search_menu_is_ready()
        return "\n".join([meal.details() for meal in self.menu])

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        # Check if the menu is ready
        self.search_menu_is_ready()

        # Check for user or registration
        if not self.search_for_client(client_phone_number):
            self.register_client(client_phone_number)

        client_obj = self.search_for_client(client_phone_number)

        # Check if all meals and quantity's exist
        self.search_all_meals(meal_names_and_quantities)

        # Order Phase
        for meal_name, quantity in meal_names_and_quantities.items():
            meal_obj = self.searched_meal_by_name(meal_name)
            client_obj.shopping_cart.append(meal_obj)
            client_obj.bill += meal_obj.price * quantity
            meal_obj.quantity -= quantity

        client_obj.ongoing_shopping_dict = meal_names_and_quantities
        return f"Client {client_phone_number} successfully ordered" \
               f" {', '.join([meal.name for meal in client_obj.shopping_cart])} for {client_obj.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):

        client_obj = self.search_for_client(client_phone_number)

        if not client_obj.shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal_name, quantity in client_obj.ongoing_shopping_dict.items():
            meal_obj = self.searched_meal_by_name(meal_name)
            meal_obj.quantity += quantity

        # clean-all
        self.clear_client_obj_bill_dict_cart(client_obj)
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):

        client_obj = self.search_for_client(client_phone_number)

        if not client_obj.shopping_cart:
            raise Exception("There are no ordered meals!")

        self.receipt_id += 1
        result_msg = f"Receipt #{self.receipt_id} with total amount of" \
                     f" {client_obj.bill:.2f} was successfully paid for {client_phone_number}."

        # clean-all
        self.clear_client_obj_bill_dict_cart(client_obj)
        return result_msg

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    # HELPERS ----------------------------------------------------------
    def search_for_client(self, p_number):
        for client in self.clients_list:
            if client.phone_number == p_number:
                return client

    def search_menu_is_ready(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def search_all_meals(self, meals_dict):
        for meal_name, ordered_quantity in meals_dict.items():

            meal_obj = self.searched_meal_by_name(meal_name)
            if not meal_obj:
                raise Exception(f"{meal_name} is not on the menu!")

            if meal_obj.quantity < ordered_quantity:
                raise Exception(f"Not enough quantity of {meal_obj.__class__.__name__}: {meal_name}!")

    def searched_meal_by_name(self, meal_name):
        for meal in self.menu:
            if meal.name == meal_name:
                return meal
        else:
            return None

    @staticmethod
    def clear_client_obj_bill_dict_cart(client_obj):
        client_obj.bill = 0.0
        client_obj.shopping_cart = []
        client_obj.ongoing_shopping_dict = {}
