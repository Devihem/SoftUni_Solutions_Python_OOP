from oop.static_and_class_methods_exercise.gym.customer import Customer
from oop.static_and_class_methods_exercise.gym.equipment import Equipment
from oop.static_and_class_methods_exercise.gym.exercise_plan import ExercisePlan
from oop.static_and_class_methods_exercise.gym.gym import Gym
from oop.static_and_class_methods_exercise.gym.subscription import Subscription
from oop.static_and_class_methods_exercise.gym.trainer import Trainer
customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)
gym = Gym()
gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)
print(Customer.get_next_id())
print(gym.subscription_info(1))
