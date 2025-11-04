from abc import ABC, abstractmethod
from project.products.base_product import BaseProduct

class BaseStore (ABC):
    def __init__ (self, name: str, location: str, capacity: int):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products: list[BaseProduct] = []
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        nameStrip = name.strip()
        if nameStrip == "":
            raise ValueError("Store name cannot be empty!")
        self.__name = nameStrip
    
    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        if ' ' in location or len(location) != 3:
            raise ValueError("Store location must be 3 chars long!")
        self.__location = location
    
    @property
    def capacity(self):
        return self.__capacity
    @capacity.setter
    def capacity(self, capacity: int):
        if capacity < 0:
            raise ValueError("Store capacity must be a positive number or 0!")
        self.__capacity = capacity
    
    def get_estimated_profit(self):
        allPrices = sum([product.price for product in self.products])
        return f"Estimated future profit for {len(self.products)} products is {(allPrices * 0.1):.2f}"

    @property
    @abstractmethod
    def store_type(self):
        pass

    @abstractmethod
    def store_stats(self):
        pass
