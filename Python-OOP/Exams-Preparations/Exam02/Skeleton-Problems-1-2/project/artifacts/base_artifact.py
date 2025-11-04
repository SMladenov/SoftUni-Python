from abc import ABC, abstractmethod

class BaseArtifact (ABC):
    def __init__ (self, name: str, price: float, space_required: int):
        self.name = name
        self.price = price
        self.space_required = space_required
    
    @property
    def name (self):
        return self.__name
    @name.setter
    def name (self, name: str):
        nameStrip = name.strip()
        if nameStrip == "" or nameStrip is None:
            raise ValueError("Artifact name cannot be null or empty!")
        else:
            self.__name = nameStrip
    
    @property
    def price (self):
        return self.__price
    @price.setter
    def price (self, price: float):
        if price <= 0:
            raise ValueError("Artifact price should be more than 0.0!")
        else:
            self.__price = price
    
    @property
    def space_required (self):
        return self.__space_required
    @space_required.setter
    def space_required (self, space_required: int):
        if 1 <= space_required <= 1000:
            self.__space_required = space_required
        else:
            raise ValueError("Space required for the artifact exhibition must be between 1 and 1000!")

    @abstractmethod
    def artifact_information(self):
        pass
        