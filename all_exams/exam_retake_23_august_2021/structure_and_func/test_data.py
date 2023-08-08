from oop.all_exams.exam_retake_23_august_2021.structure_and_func.space_station import SpaceStation

station = SpaceStation()

print(f"\n\n# CREATING ASTRONAUTS")
print(station.add_astronaut('Biologist', 'B'))
print(station.add_astronaut('Biologist', 'B Senior'))
print(station.add_astronaut('Meteorologist', 'M'))
print(station.add_astronaut('Geodesist', 'G'))

print(f"\n\n# CREATING PLANETS")
print(station.add_planet('Mars', '1_item, 2_item, 3_item, 4_item, 5_item, 6_item',))
print(station.add_planet('Earth', 'bananas'))
print(station.add_planet('Jupiter', 'stone, gems, sand,stone, gems, sand,stone, gems, sand'))
print(station.add_planet('Fail Planet', 'stone, gems, sand,stone, gems, sand,stone, gems, sand,stone, gems, sand,stone,'
                                        ' gems,sand,stone, gems, sand,stone, gems, sand,stone, gems, sand,stone, gems,'
                                        ' sand,stone, gems, sand,stone, gems, sand,stone, gems, sand'))
print(station.add_planet('Mars', 'stone'))

print(f"\n\n# RETIRE ASTRONAUT")
print(station.retire_astronaut('B Senior'))

print(f"\n\n# ASTRONAUTS INFO ")
for a in station.astronaut_repository.astronauts:
    print(a.oxygen, a.name, a.__class__.__name__)

print(f"\n\n# ASTRONAUTS INFO - AFTER RECHARGE")
station.recharge_oxygen()
for a in station.astronaut_repository.astronauts:
    print(a.oxygen, a.name, a.__class__.__name__)

print(f"\n\n# TEST SEND ON MISSION")
print(station.send_on_mission('Mars'))
print(station.send_on_mission('Jupiter'))
print(station.send_on_mission('Earth'))
print(station.send_on_mission('Fail Planet'))

print(f"\n\n# TEST REPORT")
station.add_astronaut('Biologist', 'Mr.Empty Backpack')
print(station.report())


#
# # CREATING ASTRONAUTS
# Successfully added Biologist: B.
# Successfully added Biologist: B Senior.
# Successfully added Meteorologist: M.
# Successfully added Geodesist: G.
#
#
# # CREATING PLANETS
# Successfully added Planet: Mars.
# Successfully added Planet: Earth.
# Successfully added Planet: Jupiter.
# Successfully added Planet: Fail Planet.
# Mars is already added.
#
#
# # RETIRE ASTRONAUT
# Astronaut B Senior was retired!
#
#
# # ASTRONAUTS INFO
# 70 B Biologist
# 90 M Meteorologist
# 50 G Geodesist
#
#
# # ASTRONAUTS INFO - AFTER RECHARGE
# 80 B Biologist
# 100 M Meteorologist
# 60 G Geodesist
#
#
# # TEST SEND ON MISSION
# Planet: Mars was explored. 1 astronauts participated in collecting items.
# Planet: Jupiter was explored. 1 astronauts participated in collecting items.
# Planet: Earth was explored. 1 astronauts participated in collecting items.
# Mission is not completed.
#
#
# # TEST REPORT
# 3 successful missions!
# 1 missions were not completed!
# Astronauts' info:
# Name: B
# Oxygen: 0
# Backpack items: sand, gems, sand,stone, gems, sand,stone, gems, stone, gems, sand,stone, gems, sand,stone, gems, sand,stone, gems, sand,stone, gems
# Name: M
# Oxygen: 10
# Backpack items: 6_item, 5_item, 4_item, 3_item, 2_item, 1_item
# Name: G
# Oxygen: 0
# Backpack items: bananas, sand, gems, sand,stone, gems, sand,stone
# Name: Mr.Empty Backpack
# Oxygen: 70
# Backpack items: none
#
# Process finished with exit code 0
