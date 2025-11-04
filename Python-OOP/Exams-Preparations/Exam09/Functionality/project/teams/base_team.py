from abc import ABC, abstractmethod
from project.equipment.base_equipment import BaseEquipment

class BaseTeam (ABC):
    def __init__ (self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment: list[BaseEquipment] = []

    @property
    def name (self):
        return self.__name
    @name.setter
    def name (self, name: str):
        nameStrip = name.strip()
        if nameStrip == "":
            raise ValueError("Team name cannot be empty!")
        self.__name = nameStrip
    
    @property
    def country (self):
        return self.__country
    @country.setter
    def country (self, country: str):
        countryStrip = country.strip()
        if len(countryStrip) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = countryStrip
    
    @property
    def advantage (self):
        return self.__advantage
    @advantage.setter
    def advantage (self, advantage: int):
        if advantage <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = advantage

    @abstractmethod
    def win (self):
        pass

    def get_statistics (self):
        listToOutput = []
        listToOutput.append(f"Name: {self.name}")
        listToOutput.append(f"Country: {self.country}")
        listToOutput.append(f"Advantage: {self.advantage} points")
        listToOutput.append(f"Budget: {self.budget:.2f}EUR")
        listToOutput.append(f"Wins: {self.wins}")
        listToOutput.append(f"Total Equipment Price: {sum([equipment.price for equipment in self.equipment]):.2f}")
        listToOutput.append(f"Average Protection: {round(sum([equipment.protection for equipment in self.equipment]))}")

        return "\n".join(listToOutput)
    
