import unittest
from project.railway_station import RailwayStation
from collections import deque


class RailwayStationTests (unittest.TestCase):
    def setUp (self):
        self.station = RailwayStation("Mladost")
    
    def test_constructor_all_valid (self):
        self.assertEqual(self.station.name, "Mladost")
        self.assertEqual(self.station.arrival_trains, deque())
        self.assertEqual(self.station.departure_trains, deque())
    
    def test_name_property_raises (self):
        with self.assertRaises(ValueError) as msg:
            RailwayStation("MLA")
        self.assertEqual(str(msg.exception), "Name should be more than 3 symbols!")

    def test_new_arrival_on_board (self):
        self.station.new_arrival_on_board("Rodopi")
        self.assertEqual(self.station.arrival_trains[0], "Rodopi")

    def test_train_has_arrived_not_valid (self):
        self.station.new_arrival_on_board("Rodopi")
        self.station.new_arrival_on_board("Rodopi2")
        result = self.station.train_has_arrived("Rodopi2")
        self.assertEqual(result, "There are other trains to arrive before Rodopi2.")
        self.assertTrue(self.station.arrival_trains[0] != "Rodopi2")
        
    def test_train_has_arrived_valid (self):
        self.station.new_arrival_on_board("Rodopi")
        self.station.new_arrival_on_board("Rodopi2")
        result = self.station.train_has_arrived("Rodopi")
        self.assertEqual(result, "Rodopi is on the platform and will leave in 5 minutes.")
        self.assertTrue(self.station.arrival_trains[0], "Rodopi")
    
    def test_train_has_left_True (self):
        self.station.new_arrival_on_board("Rodopi")
        self.station.new_arrival_on_board("Rodopi2")
        self.station.train_has_arrived("Rodopi")
        result = self.station.train_has_left("Rodopi")
        self.assertEqual(True, result)
        self.assertEqual(0, len(self.station.departure_trains))
    
    def test_train_has_left_False (self):
        self.station.new_arrival_on_board("Rodopi")
        self.station.new_arrival_on_board("Rodopi2")
        self.station.train_has_arrived("Rodopi")
        result = self.station.train_has_left("Rodopi2")
        self.assertEqual(False, result)
        self.assertEqual(1, len(self.station.departure_trains))

if __name__ == '__main__':
    unittest.main()