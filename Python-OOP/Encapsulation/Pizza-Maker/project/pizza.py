from project.dough import Dough
from project.topping import Topping

class Pizza:
    def __init__ (self, name: str, dough: Dough, max_number_of_toppings: int, toppings: dict = None):
        self.name = name
        self.dough: Dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings = {} if toppings is None else toppings
        self.currentToppings = 0

    @property
    def name (self):
        return self.__name
    
    @property
    def dough (self):
        return self.__dough
    
    @property
    def max_number_of_toppings (self):
        return self.__max_number_of_toppings
    
    @name.setter
    def name (self, name):
        if name == "":
            raise ValueError (f"The name cannot be an empty string")
        else:
            self.__name = name

    @dough.setter
    def dough (self, dough):
        if dough is None:
            raise ValueError (f"You should add dough to the pizza")
        else:
            self.__dough = dough

    @max_number_of_toppings.setter
    def max_number_of_toppings (self, max_number_of_toppings):
        if max_number_of_toppings <= 0:
            raise ValueError (f"The maximum number of toppings cannot be less or equal to zero")
        else:
            self.__max_number_of_toppings = max_number_of_toppings
    
    def add_topping(self, topping: Topping):
        if self.currentToppings < self.__max_number_of_toppings:
            if topping.topping_type in self.toppings.keys():
                self.toppings[topping.topping_type] += topping.weight
            else:
                self.toppings[topping.topping_type] = topping.weight
                self.currentToppings += 1
        else:
            raise ValueError (f"Not enough space for another topping")
    
    def calculate_total_weight (self):
        toppingsWeight = sum({value for value in self.toppings.values()})
        totalWeight = self.dough.weight + toppingsWeight
        return totalWeight

