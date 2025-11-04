from project.motorcycle import Motorcycle

class CrossMotorcycle (Motorcycle):
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)

    def drive (self, kilometers):
        currentFuelConsumption = kilometers * self.fuel_consumption
        if self.fuel - currentFuelConsumption >= 0:
            self.fuel -= currentFuelConsumption
