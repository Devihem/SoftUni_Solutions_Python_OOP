from oop.all_exams.exam_10_april_2022.structure_and_func.controller import Controller
from oop.all_exams.exam_10_april_2022.structure_and_func.player import Player
from oop.all_exams.exam_10_april_2022.structure_and_func.supply.drink import Drink
from oop.all_exams.exam_10_april_2022.structure_and_func.supply.food import Food

controller = Controller()
apple = Food("apple", 22)
cheese = Food("cheese")
juice = Drink("orange juice")
water = Drink("water")
first_player = Player('Peter', 15)
second_player = Player('Lilly', 12, 94)
print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
print(controller.add_player(first_player, second_player))
print(controller.duel("Peter", "Lilly"))
print(controller.add_player(first_player))
print(controller.sustain("Lilly", "Drink"))
first_player.stamina = 0
print(controller.duel("Peter", "Lilly"))
print(first_player)
print(second_player)
controller.next_day()
print(controller)