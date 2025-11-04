from project.trip import Trip
import unittest

class TripTests (unittest.TestCase):

    def setUp (self):
        self.trip = Trip(5000, 4, True)
    
    def test_constructor_all_valid (self):
        self.assertEqual(self.trip.budget, 5000)
        self.assertEqual(self.trip.travelers, 4)
        self.assertEqual(self.trip.is_family, True)
        self.assertEqual(self.trip.booked_destinations_paid_amounts, {})
    
    def test_travelers_property_raises (self):
        with self.assertRaises(ValueError) as msg:
            Trip(5000, 0, True)
        self.assertEqual(str(msg.exception), 'At least one traveler is required!')

    def test_is_family_False_under_2_travelers (self):
        trip = Trip(5000, 1, True)
        self.assertEqual(trip.is_family, False)
    
    def test_book_a_trip_destination_not_in_destinations (self):
        result = self.trip.book_a_trip("Mladost")
        self.assertEqual(result, 'This destination is not in our offers, please choose a new one!')
    
    def test_book_a_trip_not_enough_money (self):
        result = self.trip.book_a_trip("Brazil")
        self.assertEqual(result, 'Your budget is not enough!')
    
    def test_book_a_trip_all_valid (self):
        result = self.trip.book_a_trip("Bulgaria")
        self.assertEqual(result, f'Successfully booked destination Bulgaria! Your budget left is {self.trip.budget:.2f}')

    def test_book_a_trip_family_discount(self):
        trip = Trip(11000, 2, True)
        result = trip.book_a_trip("Australia")
        expected_price = 5700 * 2 * 0.9
        self.assertEqual(result, f'Successfully booked destination Australia! Your budget left is {trip.budget:.2f}')
        self.assertEqual(trip.budget, 11000 - expected_price)

    def test_booking_status_no_vacation (self):
        result = self.trip.booking_status()
        self.assertEqual(result, f'No bookings yet. Budget: {self.trip.budget:.2f}')
    
    def test_book_a_trip_not_enough_money_after_discount(self):
        trip = Trip(1000, 3, True)
        result = trip.book_a_trip("Brazil")
        self.assertEqual(result, 'Your budget is not enough!')
    
    def test_book_a_trip_no_budget_left(self):
        trip = Trip(5000, 1, False)
        trip.book_a_trip("Bulgaria")
        result = trip.book_a_trip("Brazil")
        self.assertEqual(result, 'Your budget is not enough!')
    
    def test_book_a_trip_negative_budget(self):
        trip = Trip(1000, 1, False)
        trip.book_a_trip("Brazil")
        self.assertEqual(trip.budget, 1000)
    
    def test_booking_status_all_valid (self):
        trip = Trip(18000, 1, False)
        trip.book_a_trip("Bulgaria")
        trip.book_a_trip("Brazil")
        result = []
        sorted_bookings = sorted(trip.booked_destinations_paid_amounts.items())
        for booked_destination, paid_amount in sorted_bookings:
            result.append(f"""Booked Destination: {booked_destination}
Paid Amount: {paid_amount:.2f}""")
        result.append(f"""Number of Travelers: {trip.travelers}
Budget Left: {trip.budget:.2f}""")
        
        expectedResult = "\n".join(result)
        actualResult = trip.booking_status()

        self.assertEqual(actualResult, expectedResult)

if __name__ == '__main__':
    unittest.main()
