def choose_func(nums: list, func1, func2):
    if all(num > 0 for num in nums):
        result = func1(nums)
    else:
        result = func2(nums)
    return result

# Assertions
nums1 = [1, 2, 3, 4, 5, 6]
nums2 = [1, -2, 3, -4, 5, 7]
nums3 = [-1, 2, -3, 4, 5, 0]

def square_nums(nums):
    numbers_list = list(map(lambda x: x * x, nums))
    print (numbers_list)
    return numbers_list

def remove_negatives(nums):
    numbers_list = list(filter(lambda x: x > 0, nums))
    print (numbers_list)
    return numbers_list

choose_func(nums1, square_nums, remove_negatives)
choose_func(nums2, square_nums, remove_negatives)
choose_func(nums3, square_nums, remove_negatives)




import unittest

class TestChooseFunc(unittest.TestCase):

    def test_positive_numbers(self):
        nums = [1, 2, 3, 4, 5]
        result = choose_func(nums, square_nums, remove_negatives)
        expected = [1, 4, 9, 16, 25]
        self.assertEqual(result, expected)
    
    def test_negative_numbers_with_zero(self):
        nums = [-1, 2, -3, 4, 5, 0]
        result = choose_func(nums, square_nums, remove_negatives)
        expected = [2, 4, 5]
        self.assertEqual(result, expected)

    def test_negative_numbers(self):
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