from oop.all_exams.exam_15_august_2021.structure_and_func.bakery import Bakery

bakery = Bakery("Sunny")

print(f"\n\n{'# ADD_FOOD'}")
print(bakery.add_food("Bread", "Sour", 1.50))
print(bakery.add_food("Bread", "White", 1.30))
print(bakery.add_food("Cake", "Chocolate", 2.90))
print(bakery.add_food("Cake", "Vanilla", 2.90))

print(f"\n\n{'# ADD_DRINK'}")
print(bakery.add_drink("Water", "Spring", 250, "Bankya"))
print(bakery.add_drink("Water", "Mineral", 500, "Devin"))
print(bakery.add_drink("Tea", "Black", 250, "Ahmad Tea"))
print(bakery.add_drink("Tea", "Green", 250, "Lipton"))

print(f"\n\n{'# ADD_TABLE'}")
print(bakery.add_table("OutsideTable", 52, 10))
print(bakery.add_table("OutsideTable", 95, 15))
print(bakery.add_table("InsideTable", 15, 15))
print(bakery.add_table("InsideTable", 4, 15))

print(f"\n\n{'# RESERVE_TABLE'}")
print(bakery.reserve_table(12))

print(f"\n\n{'# ORDERS_FOOD'}")
print(bakery.order_food(95, "Sour", "White", "Chocolate", "Vanilla", "Strawberry", "Hazelnut", "Wholegrain"))
print(bakery.order_food(34, "Sour", "White", "Chocolate", "Vanilla", "Strawberry", "Hazelnut", "Wholegrain"))

print(f"\n\n{'# ORDERS_DRINK'}")
print(bakery.order_drink(95, "Spring", "Mineral", "Black", "Green", "White", "Tap", "Fruit"))

print(f"\n\n{'# LEAVE_TABLE'}")
print(bakery.leave_table(95))

print(f"\n\n{'# GET_TOTAL_INCOME'}")
print(bakery.get_total_income())

print(f"\n\n{'# TABLES_INFO'}")
print(bakery.get_free_tables_info())
#
# #
# # ADD_FOOD
# Added Sour (Bread) to the food menu
# Added White (Bread) to the food menu
# Added Chocolate (Cake) to the food menu
# Added Vanilla (Cake) to the food menu
#
#
# # ADD_DRINK
# Added Spring (Bankya) to the drink menu
# Added Mineral (Devin) to the drink menu
# Added Black (Ahmad Tea) to the drink menu
# Added Green (Lipton) to the drink menu
#
#
# # ADD_TABLE
# Added table number 52 in the bakery
# Added table number 95 in the bakery
# Added table number 15 in the bakery
# Added table number 4 in the bakery
#
#
# # RESERVE_TABLE
# Table 95 has been reserved for 12 people
#
#
# # ORDERS_FOOD
# Table 95 ordered:
#  - Sour: 200.00g - 1.50lv
#  - White: 200.00g - 1.30lv
#  - Chocolate: 245.00g - 2.90lv
#  - Vanilla: 245.00g - 2.90lv
# Sunny does not have in the menu:
# Strawberry
# Hazelnut
# Wholegrain
# Could not find table 34
#
#
# # ORDERS_DRINK
# Table 95 ordered:
#  - Spring Bankya - 250.00ml - 1.50lv
#  - Mineral Devin - 500.00ml - 1.50lv
#  - Black Ahmad Tea - 250.00ml - 2.50lv
#  - Green Lipton - 250.00ml - 2.50lv
# Sunny does not have in the menu:
# White
# Tap
# Fruit
#
#
# # LEAVE_TABLE
# Table: 95
# Bill: 16.60
#
#
# # GET_TOTAL_INCOME
# Total income: 16.60lv
#
#
# # TABLES_INFO
# Table: 52
# Type: OutsideTable
# Capacity: 10
# Table: 95
# Type: OutsideTable
# Capacity: 15
# Table: 15
# Type: InsideTable
# Capacity: 15
# Table: 4
# Type: InsideTable
# Capacity: 15