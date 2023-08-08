from encapsulation_exercise.pizza_maker.dough import Dough
from encapsulation_exercise.pizza_maker.pizza import Pizza
from encapsulation_exercise.pizza_maker.topping import Topping
#
#
# tomato_topping = Topping("Tomato", 60)
# print(tomato_topping.topping_type)
# print(tomato_topping.weight)
#
# mushrooms_topping = Topping("Mushroom", 75)
# print(mushrooms_topping.topping_type)
# print(mushrooms_topping.weight)
#
# mozzarella_topping = Topping("Mozzarella", 80)
# print(mozzarella_topping.topping_type)
# print(mozzarella_topping.weight)
#
# cheddar_topping = Topping("Cheddar", 150)
#
# pepperoni_topping = Topping("Pepperoni", 120)
#
# white_flour_dough = Dough("White Flour", "Mixing", 200)
# print(white_flour_dough.flour_type)
# print(white_flour_dough.weight)
# print(white_flour_dough.baking_technique)
#
# whole_wheat_dough = Dough("Whole Wheat Flour", "Mixing", 200)
# print(whole_wheat_dough.weight)
# print(whole_wheat_dough.flour_type)
# print(whole_wheat_dough.baking_technique)
#
# p = Pizza("Margherita", whole_wheat_dough, 2)
#
# p.add_topping(tomato_topping)
# print(p.calculate_total_weight())
#
# p.add_topping(mozzarella_topping)
#
# print(p.calculate_total_weight())
# p.add_topping(mozzarella_topping)
#


# test 2

d = Dough("Sugar", "Mixing", 20)
t = Topping("Tomato", 20)
p = Pizza("Burger", d, 200)
p.add_topping(t)
p.add_topping(t)
print(p.calculate_total_weight())
