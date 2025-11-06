"""Task 1
Pick your solution to one of the exercises in this module. 
Design tests for this solution and write tests using unittest library. """
"""Task 1
Create your own implementation of a built-in function enumerate, named 'with_index', which takes two parameters: 
'iterable' and 'start', default is 0. Tips: see the documentation for the enumerate function"""

def with_index(iterable, start=0):
    index = start
    for item in iterable:
        yield index, item
        index += 1

print("____Word____")
for index, value in with_index(["one", "two", "three"], start=1):
    print(index, value)

print("____Char____")
for index, ch in with_index("hello", start=0):
    print(index, ch)

print("____Tuple____")
for index, item in with_index((12, 2028, 32)):
    print(index, item)

print("____Dict____")
data = {"a": 8, "b": 5, "c": 12}
for index, key in with_index(data):
    print(index, key, " = ", data[key])

print("____set____")
for index, val in with_index({"x", "y", "z"}):
    print(index, val)

print("____not iterable____")
try:
    for index, value in with_index(1234):
        print(index, value)
except TypeError as e:
    print("Error:", e)

print("____nested____")
data = [[1, 2], [3, 4], [5, 6]]
for index, sublist in with_index(data):
    print(index, sublist)

import unittest

class TestWithIndex(unittest.TestCase):

    def test_list_strings(self):
        data = ["a", "b", "c"]
        result = list(with_index(data))
        expected = [(0, "a"), (1, "b"), (2, "c")]
        self.assertEqual(result, expected)

    def test_start_from_index(self):
        data = [10, 20, 30]
        result = list(with_index(data, start=5))
        expected = [(5, 10), (6, 20), (7, 30)]
        self.assertEqual(result, expected)

    def test_empty(self):
        data = []
        result = list(with_index(data))
        expected = []
        self.assertEqual(result, expected)

    def test_tuple(self):
        data = ("x", "y")
        result = list(with_index(data))
        expected = [(0, "x"), (1, "y")]
        self.assertEqual(result, expected)

    def test_string(self):
        data = "hi"
        result = list(with_index(data, start=1))
        expected = [(1, "h"), (2, "i")]
        self.assertEqual(result, expected)

    def test_generator(self):
        data = (i for i in range(3))
        result = list(with_index(data))
        expected = [(0, 0), (1, 1), (2, 2)]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()