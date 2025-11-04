from cat import Cat
import unittest

class CatTests (unittest.TestCase):

    def setUp(self):
        self.cat = Cat("PisiPisi")

    def test_init(self):

        self.assertEqual(self.cat.name, "PisiPisi")
        self.assertTrue(isinstance(self.cat, Cat))

    def test_cat_after_eating (self):
        expectedSize = self.cat.size + 1
        self.cat.eat()
        self.assertEqual(self.cat.fed, True)
        self.assertEqual(self.cat.sleepy, True)
        self.assertEqual(self.cat.size, expectedSize)

    def test_cat_already_fed (self):
        self.cat.fed = True
        
        with self.assertRaises(Exception) as msg:
            self.cat.eat()
        self.assertEqual(str(msg.exception), "Already fed.")
    
    def test_cat_sleep (self):
        self.cat.eat()
        self.cat.sleep()
        self.assertEqual(self.cat.sleepy, False)

    def test_cat_cannot_sleep (self):
        self.cat.fed = False

        with self.assertRaises(Exception) as msg:
            self.cat.sleep()
        self.assertEqual(str(msg.exception), "Cannot sleep while hungry")
    
if __name__ == '__main__':
    unittest.main()