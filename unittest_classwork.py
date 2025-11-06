"""
A simple calculator.

Create a function called make_operation, which takes in a simple arithmetic operator
as a first parameter (to keep things simple let it only be '+', '-' or '*')
and an arbitrary number of arguments (only numbers) as the second parameter.
Then return the sum or product of all the numbers in the arbitrary parameter.

For example:

the call make_operation('+', 7, 7, 2) should return 16
the call make_operation('-', 5, 5, -10, -20) should return -30
the call make_operation('*', 7, 6) should return 42
"""

def make_operation(operation, *args):
    if operation == '/':
        raise TypeError("This operation is not supporsed; Use one of +-*")
    for arg in args:
        if type(arg) is not int:
            raise ValueError("One of the aruguments is not an integer: " + str(arg) )
    if operation == '+':
        return sum(args)
    if operation == '*':
        res = 1
        for x in args:
            res *= x
        return res
    if operation == '-':
        ...

import unittest


class SimpleCalculatorTest(unittest.TestCase):

    set_of_allowed_operations_ = ('+', '-', '*')

    def test_only_numbers(self):
        make_operation('+', 1, 2, 3, 4)
    
    def test_non_integer_argument_raises_error(self):
        with self.assertRaises(ValueError):
            make_operation('+', 1, 2, 3, "a")
    
    def test_more_than_3_arguments(self):
        make_operation('+', 1, 2, 3, 4)

    def test_add_sucess(self):
        result = make_operation('+', 7, 7, 2)
        expected_result = 16
        self.assertEqual(result, expected_result)

    def test_sub_sucess(self):
        result = make_operation('-', 5, 5, -10, -20)
        expected_result = 30
        self.assertEqual(result, expected_result)

    def test_mul_sucess(self):
        result = make_operation('*', 7, 6)
        expected_result = 42
        self.assertEqual(result, expected_result)

    def test_operation_is_allowed(self):
        with self.assertRaises(TypeError):
            make_operation('/', 1, 1, 1)


if __name__ == '__main__':
    unittest.main()


import unittest

class Animal:
    def talk(self):
        return "Animal makes a sound"
    
    def can_climb_tree(self):
        return self.climber

class Cat(Animal):
    def __init__(self):
        self.climber = True
    def talk(self):
        return "meow"

class Dog(Animal):
    def __init__(self):
        self.climber = False
    def talk(self):
        return "woof woof"

def animal_talk(animal: Animal):
    animal.talk()

# -----
class TestDog(unittest.TestCase):
    def setUp(self):
        self.dog = Dog()

    def test_dog_talk(self):
        self.assertEqual(self.dog.talk(), "woof woof")
    
    def test_cat_can_climb_tree(self):
        self.assertFalse(self.dog.can_climb_tree())


class TestCat(unittest.TestCase):
    def setUp(self):
        self.cat = Cat()

    def test_cat_talk(self):
        self.assertEqual(self.cat.talk(), "meow")
    
    def test_cat_can_climb_tree(self):
        self.assertTrue(self.cat.can_climb_tree())


if __name__ == "__main__":
    unittest.main()