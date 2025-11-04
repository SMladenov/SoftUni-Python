from abc import ABC, abstractmethod

class BaseClimber (ABC):
    def __init__ (self, name: str, strength: float):
        self.name = name
        self.strength = strength
        self.conquered_peaks: list = []
        self.is_prepared = True
    
    @property
    def name (self):
        return self.__name
    @name.setter
    def name (self, name: str):
        nameStrip = name.strip()
        if nameStrip == "":
            raise ValueError("Climber name cannot be null or empty!")
        self.__name = nameStrip
    
    @property
    def strength (self):
        return self.__strength
    @strength.setter
    def strength (self, strength: float):
        if strength < 0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")
        self.__strength = strength
    
    @abstractmethod
    def can_climb (self):
        pass

    @abstractmethod
    def climb (self, peak):
        pass

    def rest (self):
        self.strength += 15
    
    def __str__ (self):
        return f"{self.__class__.__name__}: /// Climber name: {self.name} * Left strength: {self.strength:.1f} * Conquered peaks: {', '.join(self.conquered_peaks)} ///"
