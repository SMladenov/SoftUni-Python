class Topping:
    def __init__ (self, topping_type: str, weight: float):
        self.topping_type = topping_type
        self.weight = weight
    
    @property
    def topping_type (self):
        return self.__topping_type
    
    @property
    def weight (self):
        return self.__weight
    
    @topping_type.setter
    def topping_type (self, topping_type):
        if topping_type == "":
            raise ValueError (f"The topping type cannot be an empty string")
        else:
            self.__topping_type = topping_type

    @weight.setter
    def weight (self, weight):
        if weight <= 0:
            raise ValueError (f"The weight cannot be less or equal to zero")
        else:
            self.__weight = weight


