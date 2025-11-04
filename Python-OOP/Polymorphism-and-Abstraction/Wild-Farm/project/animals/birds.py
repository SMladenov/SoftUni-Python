from project.animals.animal import Bird
from project.food import Fruit, Vegetable, Meat, Seed

class Owl (Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
    
    def make_sound (self):
        return "Hoot Hoot"

    def feed (self, food):
        if isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += food.quantity * 0.25
        else:
            return f"Owl does not eat {food.__class__.__name__}!"

class Hen (Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
    
    def make_sound(self):
        return "Cluck"

    def feed (self, food):
        if isinstance(food, (Fruit, Vegetable, Meat, Seed)):
            self.food_eaten += food.quantity
            self.weight += food.quantity * 0.35
        

