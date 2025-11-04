from project.vehicle import Vehicle

class Motorcycle (Vehicle):
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        
    
    def drive (self, kilometers):
        currentFuelConsumption = kilometers * self.fuel_consumption
        if self.fuel - currentFuelConsumption >= 0:
            self.fuel -= currentFuelConsumption
        

# motor1 = Motorcycle(50, 150)

# print (f"The Default Fuel Consumption for the Motor is: {motor1.DEFAULT_FUEL_CONSUMPTION}")