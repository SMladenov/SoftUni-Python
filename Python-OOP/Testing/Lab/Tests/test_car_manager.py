from car_manager import Car
import unittest

class IntegerListTests (unittest.TestCase):
    

    def test_constructor_all_valid (self):
        car = Car("Mazda", "3", 10, 55)
        self.assertTrue(isinstance(car, Car))
        self.assertEqual(car.make, "Mazda")
        self.assertEqual(car.model, "3")
        self.assertEqual(car.fuel_consumption, 10)
        self.assertEqual(car.fuel_capacity, 55)
        self.assertEqual(car.fuel_amount, 0)

    def test_constructor_invalid_make (self):
        with self.assertRaises(Exception) as msg:
            Car("", "3", 10, 55)
        
        self.assertEqual(str(msg.exception), "Make cannot be null or empty!")

        with self.assertRaises(Exception) as msg:
            Car(None, "3", 10, 55)
        self.assertEqual(str(msg.exception), "Make cannot be null or empty!")
    
    def test_constructor_invalid_model (self):
        with self.assertRaises(Exception) as msg:
            Car("Mazda", "", 10, 55)
        
        self.assertEqual(str(msg.exception), "Model cannot be null or empty!")

        with self.assertRaises(Exception) as msg:
            Car("Mazda", None, 10, 55)
        self.assertEqual(str(msg.exception), "Model cannot be null or empty!")


    def test_constructor_invalid_fuel_consumption (self):
        with self.assertRaises(Exception) as msg:
            Car("Mazda", "3", 0, 55)
        
        self.assertEqual(str(msg.exception), "Fuel consumption cannot be zero or negative!")

        with self.assertRaises(Exception) as msg:
            Car("Mazda", "3", -1, 55)
        self.assertEqual(str(msg.exception), "Fuel consumption cannot be zero or negative!")


    def test_constructor_invalid_fuel_capacity (self):
        with self.assertRaises(Exception) as msg:
            Car("Mazda", "3", 10, 0)
        
        self.assertEqual(str(msg.exception), "Fuel capacity cannot be zero or negative!")

        with self.assertRaises(Exception) as msg:
            Car("Mazda", "3", 10, -1)
        self.assertEqual(str(msg.exception), "Fuel capacity cannot be zero or negative!")

    def test_constructor_invalid_fuel_amount (self):
        car = Car("Mazda", "3", 10, 55)

        with self.assertRaises(Exception) as msg:
            car.fuel_amount = -1
        
        self.assertEqual(str(msg.exception), "Fuel amount cannot be negative!")

    def test_refuel_when_fuel_zero_or_negative (self):
        car = Car("Mazda", "3", 10, 55)

        with self.assertRaises(Exception) as msg:
            car.refuel(0)
        self.assertEqual(str(msg.exception), "Fuel amount cannot be zero or negative!")
    
        with self.assertRaises(Exception) as msg:
            car.refuel(-1)
        self.assertEqual(str(msg.exception), "Fuel amount cannot be zero or negative!")
    
    def test_refuel_when_all_ok (self):
        car = Car("Mazda", "3", 10, 55)

        car.refuel(50)
        self.assertEqual(car.fuel_amount, 50)

        car.refuel(50)
        self.assertEqual(car.fuel_amount, car.fuel_capacity)

    def test_drive_when_not_enough_fuel (self):
        car = Car("Mazda", "3", 10, 55)
        car.fuel_amount = 10

        with self.assertRaises(Exception) as msg:
            car.drive(150)
        self.assertEqual(str(msg.exception), "You don't have enough fuel to drive!")
    
    def test_drive_when_all_ok (self):
        car = Car("Mazda", "3", 10, 55)
        car.fuel_amount = 10

        car.drive(50)
        self.assertEqual(car.fuel_amount, 5)

if __name__ == '__main__':
    unittest.main()

