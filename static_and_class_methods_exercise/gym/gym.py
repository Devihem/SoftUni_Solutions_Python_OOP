from oop.static_and_class_methods_exercise.gym.customer import Customer
from oop.static_and_class_methods_exercise.gym.equipment import Equipment
from oop.static_and_class_methods_exercise.gym.exercise_plan import ExercisePlan
from oop.static_and_class_methods_exercise.gym.subscription import Subscription
from oop.static_and_class_methods_exercise.gym.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []  # obj
        self.trainers = []  # obj
        self.equipment = []  # obj
        self.plans = []  # obj
        self.subscriptions = []  # obj

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        current_subs = next(filter(lambda k: k.id == subscription_id, self.subscriptions))
        current_customer = next(filter(lambda k: k.id == current_subs.customer_id, self.customers))
        current_trainer = next(filter(lambda k: k.id == current_subs.trainer_id, self.trainers))
        current_exercise = next(filter(lambda k: k.id == current_subs.exercise_id, self.plans))
        current_equipment = next(filter(lambda k: k.id == current_exercise.equipment_id, self.equipment))

        result = [current_subs,
                  current_customer,
                  current_trainer,
                  current_equipment,
                  current_exercise]

        result = [str(x) for x in result]
        return '\n'.join(result)
