from project.vehicle import Vehicle
import unittest

class VehicleTests (unittest.TestCase):
    
    def setUp (self):
        self.vehicle = Vehicle(10.0, 155.5)
    
    def test_constructor_all_valid (self):
        self.assertEqual(self.vehicle.fuel, 10.0)
        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual(self.vehicle.horse_power, 155.5)
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)
    
    def test_drive_when_not_enough_fuel_raises (self):
        with self.assertRaises(Exception) as msg:
            self.vehicle.drive(100)
        self.assertEqual(str(msg.exception), "Not enough fuel")
    
    def test_drive_when_all_ok (self):
        self.vehicle.drive(5)
        self.assertEqual(self.vehicle.fuel, 3.75)
    
    def test_refuel_when_too_much_fuel_raises (self):
        self.vehicle.drive(5)
        
        with self.assertRaises(Exception) as msg:
            self.vehicle.refuel(10)
        self.assertEqual(str(msg.exception), "Too much fuel")

    def test_refuel_when_all_ok (self):
        self.vehicle.drive(5)
        self.vehicle.refuel(5)
        self.assertEqual(self.vehicle.fuel, 8.75)

    def test_str_dunder (self):
        result = self.vehicle.__str__()

        expectedResult = f"The vehicle has {self.vehicle.horse_power} " \
            f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        self.assertEqual(result, expectedResult)


if __name__ == '__main__':
    unittest.main()

