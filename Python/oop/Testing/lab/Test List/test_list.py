import unittest

from project.list import IntegerList


class TestIntegerList(unittest.TestCase):

    def setUp(self):
        self.test_list_empty = IntegerList()
        self.test_list_valid_parameters = IntegerList(2, 8, 3, -6)
        self.test_list_valid_and_invalid_parameters = IntegerList(2, 8, 's', 3, 4.2)

    def test_initialization_with_arguments_and_without(self):
        self.assertEqual(self.test_list_empty.get_data(), [])
        self.assertEqual(self.test_list_valid_parameters.get_data(), [2, 8, 3, -6])
        self.assertEqual(self.test_list_valid_and_invalid_parameters.get_data(), [2, 8, 3])

    def test_add_method_check_if_valueError_thrown_if_not_integer_return_data(self):
        self.test_list_empty.add(5)
        self.assertEqual(self.test_list_empty.get_data(), [5])
        with self.assertRaises(ValueError) as ve:
            self.test_list_empty.add('f')
        self.assertEqual(str(ve.exception), "Element is not Integer")

    def test_remove_index_check_if_indexError_thrown_return_deleted_check_removal(self):
        self.test_list_valid_parameters.remove_index(1)
        self.assertEqual(self.test_list_valid_parameters.get_data(), [2, 3, -6])
        self.assertEqual(self.test_list_valid_parameters.remove_index(0), 2)
        with self.assertRaises(IndexError) as ie:
            self.test_list_valid_parameters.remove_index(2)
        self.assertEqual(str(ie.exception), "Index is out of range")

    def test_get_return_index_throw_indexError(self):
        self.assertEqual(self.test_list_valid_parameters.get(2), 3)
        with self.assertRaises(IndexError) as ie:
            self.test_list_valid_parameters.get(4)
        self.assertEqual(str(ie.exception), "Index is out of range")

    def test_insert_throw_indexError_throw_valueError_insert_at_position(self):
        with self.assertRaises(IndexError) as ie:
            self.test_list_valid_parameters.insert(4, -8)
        self.assertEqual(str(ie.exception), "Index is out of range")
        with self.assertRaises(ValueError) as ve:
            self.test_list_valid_parameters.insert(2, 'o')
        self.assertEqual(str(ve.exception), "Element is not Integer")
        self.test_list_valid_parameters.insert(0, 12)
        self.assertEqual(self.test_list_valid_parameters.get_data(), [12, 2, 8, 3, -6])

    def test_get_biggest(self):
        self.assertEqual(self.test_list_valid_parameters.get_biggest(), 8)

    def test_get_index(self):
        self.assertEqual(self.test_list_valid_parameters.get_index(2), 0)


if __name__ == "__main__":
    unittest.main()
