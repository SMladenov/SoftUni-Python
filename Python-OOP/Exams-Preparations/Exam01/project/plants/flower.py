from project.plants.base_plant import BasePlant

class Flower (BasePlant):
    def __init__(self, name, price, water_needed, blooming_season: str):
        super().__init__(name, price, water_needed)
        self.blooming_season = blooming_season

    @property
    def blooming_season (self):
        return self.__blooming_season
    @blooming_season.setter
    def blooming_season (self, blooming_season: str):
        validSeasons = ["Spring", "Summer", "Fall", "Winter"]
        if blooming_season not in validSeasons:
            raise ValueError("Blooming season must be a valid one!")
        else:
            self.__blooming_season = blooming_season
    
    def plant_details (self):
        return f"Flower: {self.name}, Price: {self.price:.2f}, Watering: {self.water_needed}ml, Blooming Season: {self.blooming_season}"
