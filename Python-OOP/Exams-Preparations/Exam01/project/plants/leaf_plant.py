from project.plants.base_plant import BasePlant

class LeafPlant (BasePlant):
    def __init__(self, name, price, water_needed, size: str):
        super().__init__(name, price, water_needed)
        self.size = size

    @property
    def size (self):
        return self.__size
    @size.setter
    def size (self, size: str):
        validSizes = ["S", "M", "L"]
        if size not in validSizes:
            raise ValueError("Size must be a valid one!")
        else:
            self.__size = size
    
    def plant_details(self):
        return f"Leaf Plant: {self.name}, Price: {self.price:.2f}, Watering: {self.water_needed}ml, Size: {self.size}"
    