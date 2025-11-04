import unittest
from project.restaurant import Restaurant

class RestaurantTests (unittest.TestCase):
    
    def setUp(self):
        self.restaurant = Restaurant("Mladost1", 55)

    def test_constructor_all_valid (self):
        self.assertEqual(self.restaurant.name, "Mladost1")
        self.assertEqual(self.restaurant.capacity, 55)
        self.assertEqual(self.restaurant.waiters, [])
    
    def test_name_property_raises (self):
        with self.assertRaises(ValueError) as msg:
            Restaurant("", 55)
        self.assertEqual(str(msg.exception), "Invalid name!")

    def test_capacity_property_raises (self):
        with self.assertRaises(ValueError) as msg:
            Restaurant("Mladost1", -1)
        self.assertEqual(str(msg.exception), "Invalid capacity!")

    def test_add_waiter_no_more_place (self):
        restaurant = Restaurant("Mladost1", 2)
        restaurant.waiters = [{'name': 'Kircho'}, {'name': 'Pencho'}]
        result = restaurant.add_waiter('Dragancho')
        self.assertEqual(result, "No more places!")

    def test_add_waiter_existing_waiter (self):
        restaurant = Restaurant("Mladost1", 3)
        restaurant.waiters = [{'name': 'Kircho'}, {'name': 'Pencho'}]
        result = restaurant.add_waiter('Kircho')
        self.assertEqual(result, f"The waiter Kircho already exists!")

    def test_add_waiter_success (self):
        restaurant = Restaurant("Mladost1", 3)
        restaurant.waiters = [{'name': 'Kircho'}, {'name': 'Pencho'}]
        result = restaurant.add_waiter('Dragancho')
        self.assertEqual(result, f"The waiter Dragancho has been added.")
        self.assertEqual(restaurant.waiters, [{'name': 'Kircho'}, {'name': 'Pencho'}, {'name': 'Dragancho'}])

    def test_remove_waiter_waiter_not_found (self):
        restaurant = Restaurant("Mladost1", 3)
        restaurant.waiters = [{'name': 'Kircho'}, {'name': 'Pencho'}]
        result = restaurant.remove_waiter('Dragancho')
        self.assertEqual(result, f"No waiter found with the name Dragancho.")
    
    def test_remove_waiter_success (self):
        restaurant = Restaurant("Mladost1", 3)
        restaurant.waiters = [{'name': 'Kircho'}, {'name': 'Pencho'}]
        result = restaurant.remove_waiter('Pencho')
        self.assertEqual(result, f"The waiter Pencho has been removed.")
    
    def test_get_total_earnings (self):
        restaurant = Restaurant("Mladost1", 3)
        restaurant.waiters = [{'name': 'Kircho', 'total_earnings': 100}, {'name': 'Pencho', 'total_earnings': 200}]
        result = restaurant.get_total_earnings()
        self.assertEqual(result, 300)
    
    def test_get_waiters (self):
        restaurant = Restaurant("Mladost1", 3)
        restaurant.waiters = [{'name': 'Kircho', 'total_earnings': 100}, 
                              {'name': 'Pencho', 'total_earnings': 200},
                              {'name': 'Pencho2', 'total_earnings': 98},
                              {'name': 'Kircho2', 'total_earnings': 299}
                              ]
        result = restaurant.get_waiters(98, 150)
        expectedResult = [{'name': 'Kircho', 'total_earnings': 100},  {'name': 'Pencho2', 'total_earnings': 98}]
        self.assertEqual(result, expectedResult)

        resul2 = restaurant.get_waiters(200, 300)
        expectedResult2 = [{'name': 'Pencho', 'total_earnings': 200}, {'name': 'Kircho2', 'total_earnings': 299}]
        self.assertEqual(resul2, expectedResult2)

if __name__ == '__main__':
    unittest.main()