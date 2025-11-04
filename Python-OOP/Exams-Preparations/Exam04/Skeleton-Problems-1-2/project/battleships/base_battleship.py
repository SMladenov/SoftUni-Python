from abc import ABC, abstractmethod

class BaseBattleship(ABC):
    def __init__ (self, name: str, health: int, hit_strength: int, ammunition: int):
        self.name = name
        self.health = health
        self.hit_strength = hit_strength
        self.ammunition = ammunition
        self.is_attacking = False
        self.is_available = True

    @property
    def name(self):
        return self.__name
    @name.setter
    def name (self, name: str):
        notChar = [char for char in name if not char.isalpha()]
        if notChar:
            raise ValueError("Ship name must contain only letters!")
        self.__name = name
    
    @property
    def health (self):
        return self.__health
    @health.setter
    def health (self, health: int):
        if health < 0:
            self.__health = 0
        else:
            self.__health = health
    
    def take_damage (self, enemy_battleship):
        self.health -= enemy_battleship.hit_strength
    
    @abstractmethod
    def attack (self):
        pass

