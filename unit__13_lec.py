import unittest
from 13_21_10_function import choose_func, square_nums, remove_negatives

class TestChooseFunc(unittest.TestCase):

    def positive_numbers(self):
        nums = [1, 2, 3, 4, 5]
        result = choose_func(nums, square_nums, remove_negatives)
        expected = [1, 4, 9, 16, 25]
        self.assertEqual(result, expected)

    def negative_numbers(self):
        nums = [1, -2, 3, -4, 5]
        result = choose_func(nums, square_nums, remove_negatives)
        expected = [1, 3, 5]
        self.assertEqual(result, expected)

    def test_empty_list(self):
        nums = []
        result = choose_func(nums, square_nums, remove_negatives)
        # all([]) == True, тому викликається func1
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()