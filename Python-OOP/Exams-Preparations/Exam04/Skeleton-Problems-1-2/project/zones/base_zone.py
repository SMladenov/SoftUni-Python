from abc import ABC, abstractmethod
from project.battleships.base_battleship import BaseBattleship

class BaseZone(ABC):
    def __init__(self, code: str, volume: int):
        self.code = code
        self.volume = volume
        self.ships: list[BaseBattleship] = []
    
    @property
    def code (self):
        return self.__code
    @code.setter
    def code (self, code: str):
        isNotDigit = [char for char in code if not char.isdigit()]
        if isNotDigit:
            raise ValueError("Zone code must contain digits only!")
        self.__code = code
    
    def get_ships (self):
        return sorted(self.ships, key=lambda ship: (-ship.hit_strength, ship.name))
    
    @abstractmethod
    def zone_info (self):
        pass