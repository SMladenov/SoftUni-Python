#Tripple A pattern:
#Arrange
#Act
#Assert

#Test runner
#assertEqual()
#assertTrue()
#assertIn() - tests that the first argument is in / is not in the second
#assertRaises() - raises a specific exception
#setUp() - prepares the test fixture


import unittest
from person import Person

def sum_nums(a, b):
    return a + b

class SimpleTest (unittest.TestCase):
    def test_upper (self):
        result = 'foo'.upper()
        expected_result = 'FOO'
        self.assertEqual(result, expected_result)

class SumTest (unittest.TestCase):
    def test_sum_nums_returns_result(self):
        actual_result = sum_nums(4, 5)
        expected_result = 9
        self.assertEqual(actual_result, expected_result)

class PersonTests (unittest.TestCase):

    #To setUp the Arrange
    def setUp(self):
        self.person = Person("John", "Doe", 40)

    def test_init (self):
        #person = Person("John", "Doe", 40)
        first_name = self.person.first_name
        last_name = self.person.last_name
        age = self.person.age
        self.assertTrue(isinstance(self.person, Person))
        self.assertEqual(first_name, "John")
        self.assertEqual(last_name, "Doe")
        self.assertEqual(age, 40)

    def test_full_name (self):
        #Arrange
        #person = Person("John", "Doe", 40)
        #Act
        actual_result = self.person.get_full_name()
        expected_result = "John Doe"
        #Assert
        self.assertEqual(actual_result, expected_result)

    def test_get_info (self):
        #person = Person("John", "Doe", 40)
        actual_result = self.person.get_info()
        expected_result = "John Doe is 40 years old"
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()

