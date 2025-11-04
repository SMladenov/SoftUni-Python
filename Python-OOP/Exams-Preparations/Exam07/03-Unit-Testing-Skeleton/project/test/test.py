import unittest
from project.climbing_robot import ClimbingRobot

class ClimbingRobotTests (unittest.TestCase):

    def setUp (self):
        self.robot = ClimbingRobot("Mountain", "Wheel", 10, 10)
    
    def test_constructor_all_valid (self):
        self.assertEqual(self.robot.category, "Mountain")
        self.assertEqual(self.robot.part_type, "Wheel")
        self.assertEqual(self.robot.capacity, 10)
        self.assertEqual(self.robot.memory, 10)
        self.assertEqual(self.robot.installed_software, [])

    def test_category_not_in_valid_raises (self):
        with self.assertRaises(ValueError) as msg:
            ClimbingRobot("SomeOtherCategory", "Wheel", 10, 10)
        self.assertEqual(str(msg.exception), "Category should be one of ['Mountain', 'Alpine', 'Indoor', 'Bouldering']")

    def test_get_used_capacity (self):
        self.robot.installed_software = [
        {"name": "Software1", "capacity_consumption": 3, "memory_consumption": 2},
        {"name": "Software2", "capacity_consumption": 2, "memory_consumption": 1}
        ]
        self.assertEqual(self.robot.get_used_capacity(), 5)
    
    def test_get_available_capacity (self):
        self.robot.installed_software = [
        {"name": "Software1", "capacity_consumption": 3, "memory_consumption": 2},
        {"name": "Software2", "capacity_consumption": 2, "memory_consumption": 1}
        ]
        self.assertEqual(self.robot.get_available_capacity(), 5)
    
    def test_get_used_memory (self):
        self.robot.installed_software = [
        {"name": "Software1", "capacity_consumption": 3, "memory_consumption": 2},
        {"name": "Software2", "capacity_consumption": 2, "memory_consumption": 1}
        ]
        self.assertEqual(self.robot.get_used_memory(), 3)
    
    def test_get_available_memory (self):
        self.robot.installed_software = [
        {"name": "Software1", "capacity_consumption": 3, "memory_consumption": 2},
        {"name": "Software2", "capacity_consumption": 2, "memory_consumption": 1}
        ]
        self.assertEqual(self.robot.get_available_memory(), 7)

    def test_install_software_success (self):
        software = {"name": "Software1", "capacity_consumption": 4, "memory_consumption": 3}
        result = self.robot.install_software(software)

        self.assertIn(software, self.robot.installed_software)
        self.assertEqual(result, "Software 'Software1' successfully installed on Mountain part.")
    
    def test_install_software_insufficient_capacity(self):
        software = {"name": "Software2", "capacity_consumption": 11, "memory_consumption": 3}
        result = self.robot.install_software(software)

        self.assertNotIn(software, self.robot.installed_software)
        self.assertEqual(result, "Software 'Software2' cannot be installed on Mountain part.")

    def test_install_software_insufficient_memory(self):
        software = {"name": "Software3", "capacity_consumption": 4, "memory_consumption": 11}
        result = self.robot.install_software(software)

        self.assertNotIn(software, self.robot.installed_software)
        self.assertEqual(result, "Software 'Software3' cannot be installed on Mountain part.")

    def test_install_software_exact_capacity_memory(self):
        software = {"name": "Software4", "capacity_consumption": 10, "memory_consumption": 10}
        result = self.robot.install_software(software)

        self.assertIn(software, self.robot.installed_software)
        self.assertEqual(result, "Software 'Software4' successfully installed on Mountain part.")

if __name__ == '__main__':
    unittest.main()