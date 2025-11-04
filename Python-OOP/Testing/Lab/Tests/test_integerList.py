from extended_list import IntegerList
import unittest

class IntegerListTests (unittest.TestCase):

    def setUp(self):
        self.integerList = IntegerList(10, 2, 4, 5, 6, 7)

    def test_constructor(self):
        self.assertTrue(isinstance(self.integerList, IntegerList))
        actual_data = self.integerList._IntegerList__data
        #actual_data = self.integerList.get_data()
        self.assertEqual(actual_data, [10, 2, 4, 5, 6, 7])
    
    def test_constructor_no_arguments(self):
        empty_list = IntegerList()
        self.assertEqual(empty_list._IntegerList__data, [])

    def test_constructor_with_mixed_types(self):
        mixed_list = IntegerList(1, "string", 3.5, [1, 2], {5: "five"}, 10)
        self.assertEqual(mixed_list._IntegerList__data, [1, 10])

    def test_get_data(self):
        actual_data = self.integerList.get_data()
        self.assertEqual(actual_data, [10, 2, 4, 5, 6, 7])

    def test_add_throw_error(self):
        with self.assertRaises(ValueError) as msg:
            self.integerList.add("Not int")
        #Assert
        self.assertEqual(str(msg.exception), "Element is not Integer")
        #Second Assert
        result = self.integerList.get_data()
        expected = [10, 2, 4, 5, 6, 7]
        self.assertEqual(result, expected)
    
    def test_add_element_success(self):
        result_list = self.integerList.add(6)
        self.assertEqual(result_list, [10, 2, 4, 5, 6, 7, 6])
        result_data_after = self.integerList.get_data()
        self.assertEqual(result_list, result_data_after)
        self.assertEqual(self.integerList._IntegerList__data, result_list)


    

    def test_remove_index_throw_error(self):
        self.assertEqual(len(self.integerList.get_data()), 6)

        with self.assertRaises(IndexError) as msg:
            self.integerList.remove_index(6)
        self.assertEqual(str(msg.exception), "Index is out of range")

        self.assertEqual(len(self.integerList.get_data()), 6)

        with self.assertRaises(IndexError) as msg:
            self.integerList.remove_index(11)
        self.assertEqual(str(msg.exception), "Index is out of range")

        self.assertEqual(len(self.integerList.get_data()), 6)

    # def test_remove_index_empty_list_throws_error(self):
    #     empty_list = IntegerList()
    #     with self.assertRaises(IndexError) as msg:
    #         empty_list.remove_index(-1)
    #     self.assertEqual(str(msg.exception), "list index out of range")
    
    def test_remove_index_success(self):
        self.assertEqual(self.integerList.get_data()[0], 10)
        self.assertEqual(len(self.integerList.get_data()), 6)
        old_value = self.integerList.get_data()[0]

        return_value = self.integerList.remove_index(0)
        self.assertEqual(old_value, return_value)
        self.assertEqual(self.integerList.get_data()[0], 2)
        self.assertEqual(len(self.integerList.get_data()), 5)
        self.assertEqual(self.integerList.get_data(), [2, 4, 5, 6, 7])



    def test_get_invalid_index_throw_error(self):
        self.assertEqual(len(self.integerList.get_data()), 6)

        with self.assertRaises(IndexError) as msg:
            self.integerList.get(6)
        self.assertEqual(str(msg.exception), "Index is out of range")

        result = self.integerList.get_data()
        expected = [10, 2, 4, 5, 6, 7]
        self.assertEqual(result, expected)

        with self.assertRaises(IndexError) as msg:
            self.integerList.get(11)
        self.assertEqual(str(msg.exception), "Index is out of range")
    
    # def test_get_from_empty_list(self):
    #     empty_list = IntegerList()
    #     with self.assertRaises(IndexError) as msg:
    #         empty_list.get(0)
    #     self.assertEqual(str(msg.exception), "Index is out of range")

    def test_get_index_success(self):
        self.assertEqual(len(self.integerList.get_data()), 6)
        self.assertEqual(self.integerList.get_data()[0], 10)
        actual_result = self.integerList.get(0)
        self.assertEqual(actual_result, 10)
        self.assertEqual(len(self.integerList.get_data()), 6)

    def test_insert_element_throw_index_error (self):
        self.assertEqual(len(self.integerList.get_data()), 6)

        with self.assertRaises(IndexError) as msg:
            self.integerList.insert(11, 14)
        self.assertEqual(str(msg.exception), "Index is out of range")
        self.assertEqual(len(self.integerList.get_data()), 6)

        with self.assertRaises(IndexError) as msg:
            self.integerList.insert(6, 14)
        self.assertEqual(str(msg.exception), "Index is out of range")
        self.assertEqual(len(self.integerList.get_data()), 6)
    
    def test_insert_element_throw_value_error (self):
        self.assertEqual(len(self.integerList.get_data()), 6)
        with self.assertRaises(ValueError) as msg:
            self.integerList.insert(0, '14')
        self.assertEqual(str(msg.exception), 'Element is not Integer')
        self.assertEqual(len(self.integerList.get_data()), 6)
    
    def test_insert_element_success (self):
        self.assertEqual(len(self.integerList.get_data()), 6)
        self.assertEqual(self.integerList.get_data()[0], 10)

        result = self.integerList.insert(0, 14)
        modified_list = [14, 10, 2, 4, 5, 6, 7]
        actual_list = self.integerList.get_data()
        
        self.assertIsNone(result)
        self.assertEqual(modified_list, actual_list)
        self.assertEqual(self.integerList.get_data()[0], 14)
        self.assertEqual(len(self.integerList.get_data()), 7)

    def test_get_biggest(self):
        maxNum = max(self.integerList.get_data())
        actual_result = self.integerList.get_biggest()
        self.assertEqual(maxNum, actual_result)

    def test_get_biggest_empty_list_throws_index_error(self):
        empty_list = IntegerList()
        with self.assertRaises(IndexError):
            empty_list.get_biggest()

    def test_get_index(self):
        actual_index = self.integerList.get_data().index(10)
        result1 = self.integerList.get_index(10)
        self.assertEqual(actual_index, 0)
        self.assertEqual(actual_index, result1)

        self.integerList.add(10)
        self.assertEqual(self.integerList.get_data()[6], 10)
        result2 = self.integerList.get_index(10)
        self.assertEqual(result2, 0)
    
    def test_get_index_of_nonexistent_element_throws_value_error(self):
        with self.assertRaises(ValueError):
            self.integerList.get_index(444)
    
if __name__ == '__main__':
    unittest.main()