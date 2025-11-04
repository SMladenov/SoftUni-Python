from project.car import Car

class SportCar (Car):
    DEFAULT_FUEL_CONSUMPTION = 10

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = SportCar.DEFAULT_FUEL_CONSUMPTION
    
    def drive (self, kilometers):
        currentFuelConsumption = kilometers * self.fuel_consumption
        if self.fuel - currentFuelConsumption >= 0:
            self.fuel -= currentFuelConsumption
    