from project.furniture import Furniture
from typing import Tuple, Optional
import unittest


class SoccerPlayerTests (unittest.TestCase):
    
    def setUp(self):
        self.furniture = Furniture("Evtino", 99.9, (3, 3, 3), True, 55.5)

    def test_constructor_valid (self):
        self.assertEqual(self.furniture.model, "Evtino")
        self.assertEqual(self.furniture.price, 99.9)
        self.assertEqual(self.furniture.dimensions, (3, 3, 3))
        self.assertEqual(self.furniture.in_stock, True)
        self.assertEqual(self.furniture.weight, 55.5)
    
    def test_model_not_valid_raises_empty (self):
        with self.assertRaises(ValueError) as msg:
            Furniture("", 99.9, (3, 3, 3), True, 55.5)
        self.assertEqual(str(msg.exception), "Model must be a non-empty string with a maximum length of 50 characters.")
    
    def test_model_not_valid_raises_more (self):
        with self.assertRaises(ValueError) as msg:
            Furniture(f"{'*' * 60}", 99.9, (3, 3, 3), True, 55.5)
        self.assertEqual(str(msg.exception), "Model must be a non-empty string with a maximum length of 50 characters.")

    def test_price_not_valid_raises (self):
        with self.assertRaises(ValueError) as msg:
            Furniture("Evtino", -12, (3, 3, 3), True, 55.5)
        self.assertEqual(str(msg.exception), "Price must be a non-negative number.")

    def test_dimensions_not_valid_raises_len (self):
        with self.assertRaises(ValueError) as msg:
            Furniture("Evtino", 99.9, (3, 3), True, 55.5)
        self.assertEqual(str(msg.exception), "Dimensions tuple must contain 3 integers.")
    
    def test_dimensions_not_valid_raises_value (self):
        with self.assertRaises(ValueError) as msg:
            Furniture("Evtino", 99.9, (3, 3, 0), True, 55.5)
        self.assertEqual(str(msg.exception), "Dimensions tuple must contain integers greater than zero.")
    
    def test_weight_not_valid_raises (self):
        with self.assertRaises(ValueError) as msg:
            Furniture("Evtino", 99.9, (3, 3, 3), True, 0)
        self.assertEqual(str(msg.exception), "Weight must be greater than zero.")
    
    def test_get_available_status (self):
        furniture = Furniture("Evtino", 99.9, (3, 3, 3), True, 55.5)
        result = furniture.get_available_status()
        self.assertEqual(result, f"Model: {furniture.model} is currently in stock.")
    
    def test_get_available_status_not_in_stock (self):
        furniture = Furniture("Evtino", 99.9, (3, 3, 3), False, 55.5)
        result = furniture.get_available_status()
        self.assertEqual(result, f"Model: {furniture.model} is currently unavailable.")
    
    def test_get_specifications (self):
        furniture = Furniture("Evtino", 99.9, (3, 3, 3), True, 55.5)
        height, width, depth = furniture.dimensions
        result = furniture.get_specifications()
        self.assertEqual(result, f"Model: {furniture.model} has the following dimensions: {height}mm x {width}mm x {depth}mm and weighs: {furniture.weight}")
    
    def test_get_specifications (self):
        furniture = Furniture("Evtino", 99.9, (3, 3, 3), True, None)
        height, width, depth = furniture.dimensions
        result = furniture.get_specifications()
        self.assertEqual(result, f"Model: {furniture.model} has the following dimensions: {height}mm x {width}mm x {depth}mm and weighs: N/A")

if __name__ == '__main__':
    unittest.main()


