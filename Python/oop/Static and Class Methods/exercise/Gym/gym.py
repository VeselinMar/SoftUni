from typing import List

from Gym.customer import Customer
from Gym.equipment import Equipment
from Gym.exercise_plan import ExercisePlan
from Gym.subscription import Subscription
from Gym.trainer import Trainer


class Gym:

    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

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

    def subscription_info(self, subscription_id: id):
        subscription = next((subscription for subscription in self.subscriptions
                             if subscription.id == subscription_id), None).__repr__()
        customer = next((customer for customer in self.customers if customer.id == subscription_id), None).__repr__()
        trainer = next((trainer for trainer in self.trainers if trainer.id == subscription_id), None).__repr__()
        equipment = next((equipment for equipment in self.equipment
                          if equipment.id == subscription_id), None).__repr__()
        plan = next((plan for plan in self.plans if plan.id == subscription_id), None).__repr__()

        return f"{subscription}\n{customer}\n{trainer}\n{equipment}\n{plan}"
