from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer

class Gym:
    def __init__ (self):
        self.customers: list [Customer] = []
        self.trainers: list [Trainer] = []
        self.equipment: list [Equipment] = []
        self.plans: list [ExercisePlan] = []
        self.subscriptions: list [Subscription] = []
    
    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)
            return
    
    def add_trainer (self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)
            return
    
    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)
            return
        
    def add_plan (self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)
            return
        
    def add_subscription (self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)
            return

    def subscription_info (self, subscription_id: int):
        listToOutput = []

        subscription = [subscription for subscription in self.subscriptions if subscription.id == subscription_id]
        listToOutput.append(f"{subscription[0].__repr__()}")

        customer = [customer for customer in self.customers if customer.id == subscription[0].customer_id]
        listToOutput.append(f"{customer[0].__repr__()}")

        trainer = [trainer for trainer in self.trainers if trainer.id == subscription[0].trainer_id]
        listToOutput.append(f"{trainer[0].__repr__()}")

        plan = [plan for plan in self.plans if plan.id == subscription[0].exercise_id]

        equipment = [equipment for equipment in self.equipment if equipment.id == plan[0].id]
        listToOutput.append(f"{equipment[0].__repr__()}")
        listToOutput.append(f"{plan[0].__repr__()}")


        return '\n'.join(listToOutput)
    