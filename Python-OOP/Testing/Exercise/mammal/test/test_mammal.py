from project.mammal import Mammal
import unittest

class MammalTests (unittest.TestCase):
    
    def setUp (self):
        self.mammal = Mammal("Kircho", "Lion", "Raur")

    def test_constructor_all_valid (self):
        self.assertEqual(self.mammal.name, "Kircho")
        self.assertEqual(self.mammal.type, "Lion")
        self.assertEqual(self.mammal.sound, "Raur")
        self.assertEqual(self.mammal.get_kingdom(), "animals")
    
    def test_make_sound (self):
        result = self.mammal.make_sound()

        self.assertEqual(result, f"{self.mammal.name} makes {self.mammal.sound}")

    def test_get_kingdom (self):
        result = self.mammal.get_kingdom()

        self.assertEqual(result, "animals")
    
    def test_info (self):
        result = self.mammal.info()

        self.assertEqual(result, f"{self.mammal.name} is of type {self.mammal.type}")

if __name__ == '__main__':
    unittest.main()

