from project.animals.animal import Mammal
from project.food import Fruit, Vegetable, Meat, Seed

class Mouse (Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
    
    def make_sound(self):
        return "Squeak"

    def feed (self, food):
        if isinstance(food, (Vegetable, Fruit)):
            self.food_eaten += food.quantity
            self.weight += food.quantity * 0.10
        else:
            return f"Mouse does not eat {food.__class__.__name__}!"

class Dog (Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
    
    def make_sound(self):
        return "Woof!"

    def feed (self, food):
        if isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += food.quantity * 0.40
        else:
            return f"Dog does not eat {food.__class__.__name__}!"

class Cat (Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
    
    def make_sound(self):
        return "Meow"

    def feed (self, food):
        if isinstance(food, (Vegetable, Meat)):
            self.food_eaten += food.quantity
            self.weight += food.quantity * 0.30
        else:
            return f"Cat does not eat {food.__class__.__name__}!"

class Tiger (Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
    
    def make_sound(self):
        return "ROAR!!!"

    def feed (self, food):
        if isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += food.quantity * 1.00
        else:
            return f"Tiger does not eat {food.__class__.__name__}!"



