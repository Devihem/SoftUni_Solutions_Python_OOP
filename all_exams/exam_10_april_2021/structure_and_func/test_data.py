from oop.all_exams.exam_10_april_2021.structure_and_func.controller import Controller

controller = Controller()

print("\n\n# Creating AQ")
print(controller.add_aquarium("FreshwaterAquarium", "FRESH_AQ"))
print(controller.add_aquarium("SaltwaterAquarium", "SALT_AQ"))
print(controller.add_aquarium("NoWater", "No_AQ"))
print(len(controller.aquariums))

print("\n\n# Creating Deco")
print(controller.add_decoration("Ornament"))
print(controller.add_decoration("Ornament"))
print(controller.add_decoration("Plant"))
print(controller.add_decoration("Plant"))
print(controller.add_decoration("Mlant"))
print(len(controller.decorations_repository.decorations))

print("\n\n# Insert Deco")
print(controller.insert_decoration("Wrong_Name", "Plant"))
print(controller.insert_decoration("FRESH_AQ", "Plant"))
print(controller.insert_decoration("FRESH_AQ", "Plant"))
print(controller.insert_decoration("FRESH_AQ", "Plant"))
print(controller.insert_decoration("FRESH_AQ", "Wrong_Type"))

print("\n\n# Add Fish")
print(controller.add_fish("FRESH_AQ", "BananaFish", "Fish_name_2", "Species_48", 101.01))
for x in range(48):
    controller.add_fish("FRESH_AQ", "FreshwaterFish", f"Fish_name_{x}", "Species_1", 101.01)
print(controller.add_fish("FRESH_AQ", "FreshwaterFish", "Fish_name_2", "Species_48", 101.01))
print(controller.add_fish("FRESH_AQ", "SaltwaterFish", "Fish_name_3", "Species_49", 101.01))
print(controller.add_fish("FRESH_AQ", "FreshwaterFish", "Fish_name_2", "Species_50", 101.01))
print(controller.add_fish("FRESH_AQ", "FreshwaterFish", "Fish_name_2", "Species_51", 101.01))
print(controller.add_fish("FRESH_AQ", "FreshwaterFish", "Fish_name_2", "Species_52", 101.01))
print(len(controller.aquariums[0].fish))

print("\n\n# Feed Fish")
print(controller.feed_fish("FRESH_AQ"))
print(controller.feed_fish("SALT_AQ"))

print("\n\n# Calculate Value")
print(controller.calculate_value("FRESH_AQ"))
print(controller.calculate_value("SALT_AQ"))

print("\n\n# Test Report")
print(controller.report())

# EXPECTED OUTPUT

#
# # Creating AQ
# Successfully added FreshwaterAquarium.
# Successfully added SaltwaterAquarium.
# Invalid aquarium type.
# 2
#
#
# # Creating Deco
# Successfully added Ornament.
# Successfully added Ornament.
# Successfully added Plant.
# Successfully added Plant.
# Invalid decoration type.
# 4
#
#
# # Insert Deco
# There isn't a decoration of type Plant.
# Successfully added Plant to FRESH_AQ.
# Successfully added Plant to FRESH_AQ.
# There isn't a decoration of type Plant.
# There isn't a decoration of type Wrong_Type.
#
#
# # Add Fish
# There isn't a fish of type BananaFish.
# Successfully added FreshwaterFish to FRESH_AQ.
# Water not suitable.
# Successfully added FreshwaterFish to FRESH_AQ.
# Not enough capacity.
# Not enough capacity.
# 50
#
#
# # Feed Fish
# Fish fed: 50
# Fish fed: 0
#
#
# # Calculate Value
# The value of Aquarium FRESH_AQ is 5070.50.
# The value of Aquarium SALT_AQ is 0.00.
#
#
# # Test Report
# FRESH_AQ:
# Fish: Fish_name_0 Fish_name_1 Fish_name_2 Fish_name_3 Fish_name_4 Fish_name_5 Fish_name_6 Fish_name_7 Fish_name_8 Fish_name_9 Fish_name_10 Fish_name_11 Fish_name_12 Fish_name_13 Fish_name_14 Fish_name_15 Fish_name_16 Fish_name_17 Fish_name_18 Fish_name_19 Fish_name_20 Fish_name_21 Fish_name_22 Fish_name_23 Fish_name_24 Fish_name_25 Fish_name_26 Fish_name_27 Fish_name_28 Fish_name_29 Fish_name_30 Fish_name_31 Fish_name_32 Fish_name_33 Fish_name_34 Fish_name_35 Fish_name_36 Fish_name_37 Fish_name_38 Fish_name_39 Fish_name_40 Fish_name_41 Fish_name_42 Fish_name_43 Fish_name_44 Fish_name_45 Fish_name_46 Fish_name_47 Fish_name_2 Fish_name_2
# Decorations: 2
# Comfort: 10
# SALT_AQ:
# Fish: none
# Decorations: 0
# Comfort: 0
#
# Process finished with exit code 0
