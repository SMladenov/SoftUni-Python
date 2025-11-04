from abc import ABC, abstractmethod

class BasePlant (ABC):
    def __init__(self, name: str, price: float, water_needed: int):
        self.name = name
        self.price = price
        self.water_needed = water_needed
    
    @property
    def name (self):
        return self.__name
    @name.setter
    def name (self, name: str):
        nameStrip = name.strip()
        if nameStrip == "" or nameStrip is None:
            raise ValueError("Plant name cannot be null or empty!")
        else:
            self.__name = nameStrip
        
    @property
    def price (self):
        return self.__price
    @price.setter
    def price (self, price: float):
        if price <= 0:
            raise ValueError("Price must be greater than zero!")
        else:
            self.__price = price
    
    @property
    def water_needed (self):
        return self.__water_needed
    @water_needed.setter
    def water_needed (self, water_needed: int):
        if 1 <= water_needed <= 2000:
            self.__water_needed = water_needed
        else:
            raise ValueError("Water needed must be between 1 and 2000 ml!")

    @abstractmethod
    def plant_details (self):
        pass

