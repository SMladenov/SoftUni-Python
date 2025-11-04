from abc import ABC, abstractmethod

class BaseCollector (ABC):
    def __init__ (self, name: str, available_money: float, available_space: int):
        self.name = name
        self.available_money = available_money
        self.available_space = available_space
        self.purchased_artifacts: list = []
    
    @property
    def name (self):
        return self.__name
    @name.setter
    def name (self, name: str):
        if not (name[0].isalnum() and name[-1].isalnum()):
            raise ValueError("Collector name must contain letters, numbers, and optional white spaces between them!")
        
        for char in name:
            if not (char.isalnum() or char == " "):
                raise ValueError("Collector name must contain letters, numbers, and optional white spaces between them!")
        self.__name = name

    @property
    def available_money (self):
        return self.__available_money
    @available_money.setter
    def available_money (self, available_money: float):
        if available_money < 0:
            raise ValueError("A collector cannot have a negative amount of money!")
        self.__available_money = available_money
    
    @property
    def available_space (self):
        return self.__available_space
    @available_space.setter
    def available_space (self, available_space: int):
        if available_space < 0:
            raise ValueError("A collector cannot have a negative space available for exhibitions!")
        self.__available_space = available_space
    
    @abstractmethod
    def increase_money (self):
        pass
    
    def can_purchase (self, artifact_price: float, artifact_space_required: int):
        if self.available_money >= artifact_price and self.available_space >= artifact_space_required:
            return True
        else:
            return False
    
    def __str__ (self):
        if self.purchased_artifacts:
            artifacts = self.purchased_artifacts.copy()
            artifacts.sort()
            artifacts.reverse()
            return f"Collector name: {self.name}; Money available: {self.available_money}; Space available: {self.available_space}; Artifacts: {', '.join(artifacts)}"
        else:
            return f"Collector name: {self.name}; Money available: {self.available_money}; Space available: {self.available_space}; Artifacts: none"
        
        
    

    