from worker import Worker
import unittest


class WorkerTests (unittest.TestCase):
    def setUp(self):
        self.worker = Worker("John", 10, 10)

    def test_init (self):
        #Assert
        self.assertTrue(isinstance(self.worker, Worker))
        self.assertEqual(self.worker.name, "John")
        self.assertEqual(self.worker.energy, 10)
        self.assertEqual(self.worker.money, 0)
        self.assertEqual(self.worker.salary, 10)

    def test_rest (self):
        #Act
        self.worker.rest()
        actual_result = self.worker.energy
        #Assert
        self.assertEqual(actual_result, 11)
    
    def test_get_info (self):
        #Act
        actual_result = self.worker.get_info()
        #Assert
        self.assertEqual(actual_result, f'{self.worker.name} has saved {self.worker.money} money.')

    def test_negative_energy (self):
        #Arrange
        self.worker.energy = 0

        #Act & Assert
        with self.assertRaises(Exception) as msg:
            self.worker.work()

        #Assert
        self.assertEqual(str(msg.exception), "Not enough energy.")
    
    def test_money_increased_work (self):
        self.worker.work()
        self.assertEqual(self.worker.money, self.worker.salary)
    
    def test_energy_decreases_work (self):
        initialEnergy = self.worker.energy
        self.worker.work()
        self.assertEqual(self.worker.energy, initialEnergy - 1)

if __name__ == '__main__':
    unittest.main()
