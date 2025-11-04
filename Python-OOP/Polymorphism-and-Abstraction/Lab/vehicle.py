from abc import ABC, abstractmethod

class Vehicle (ABC):
    @abstractmethod
    def drive (self):
        pass

    @abstractmethod
    def refuel (self):
        pass

class Car (Vehicle):
    def __init__ (self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive (self, distance: int):
        fuelNeeded = distance * (self.fuel_consumption + 0.9)
        if fuelNeeded <= self.fuel_quantity:
            self.fuel_quantity -= fuelNeeded
    
    def refuel (self, fuel: float):
        self.fuel_quantity += fuel


class Truck (Vehicle):
    def __init__ (self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive (self, distance: int):
        fuelNeeded = distance * (self.fuel_consumption + 1.6)
        if fuelNeeded <= self.fuel_quantity:
            self.fuel_quantity -= fuelNeeded

    def refuel (self, fuel: float):
        self.fuel_quantity += fuel * 0.95

car = Car(20, 5)

car.drive(3)

print(car.fuel_quantity)

car.refuel(10)

print(car.fuel_quantity)

truck = Truck(100, 15)

truck.drive(5)

print(truck.fuel_quantity)

truck.refuel(50)

print(truck.fuel_quantity)