from project.vehicle import Vehicle

class Car (Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = Car.DEFAULT_FUEL_CONSUMPTION
    
    def drive (self, kilometers):
        currentFuelConsumption = kilometers * self.fuel_consumption
        if self.fuel - currentFuelConsumption >= 0:
            self.fuel -= currentFuelConsumption
        

# car1 = Car(50, 150)

# print (f"The Default Fuel Consumption for the Car is: {car1.DEFAULT_FUEL_CONSUMPTION}")