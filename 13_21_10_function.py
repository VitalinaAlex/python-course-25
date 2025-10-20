"""Example from lecture"""
import math
def make_cilinder_volume(r)
  dev volume(h)
    return   math.pi * r**2 * h
  return volume

volume_r10 =  make_cilinder_volume(10)

"""Task 1
Write a Python program to detect the number of local variables declared in a function."""
"""Nested function from lecture"""
def test(word):
    print (f"word = {word}")
    def low(it):
        print(f"it = {it}")
        if it.isdigit():
            return 'N'
        return it.lower()
    res = ''
    for i in word:
        res += low(i)
        print (res)
        print("Locals in function")
        print(locals())
    return res
test('Hello1')
"""
RESULT:
word = Hello1
it = H
h
Locals in function
{'word': 'Hello1', 'low': <function test.<locals>.low at 0x10323ac40>, 'res': 'h', 'i': 'H'}
it = e
he
Locals in function
{'word': 'Hello1', 'low': <function test.<locals>.low at 0x10323ac40>, 'res': 'he', 'i': 'e'}
it = l
hel
Locals in function
{'word': 'Hello1', 'low': <function test.<locals>.low at 0x10323ac40>, 'res': 'hel', 'i': 'l'}
it = l
hell
Locals in function
{'word': 'Hello1', 'low': <function test.<locals>.low at 0x10323ac40>, 'res': 'hell', 'i': 'l'}
it = o
hello
Locals in function
{'word': 'Hello1', 'low': <function test.<locals>.low at 0x10323ac40>, 'res': 'hello', 'i': 'o'}
it = 1
helloN
Locals in function
{'word': 'Hello1', 'low': <function test.<locals>.low at 0x10323ac40>, 'res': 'helloN', 'i': '1'}"""

"""Task 2
Write a Python program to access a function inside a function (Tips: use function, which returns another function)"""
def make_sentense(one_word):
  # Ця зовнішня функція повертає іншу функцію
  def make_word(second_word):
    # Внутрішня функція використовує змінну із зовнішньї функції
    return one_word + " " + second_word
  return make_word

# Створення функцій
result_one = make_sentense("Word number 1")
result_two = make_sentense("Word number 2")
result = make_sentense(result_one("Word number X"))

# Друк функції
print(result_one("Word number 3"))
print(result_two("Word number 4"))
print(result(result_two("Word number Y")))
"""
Word number 1 Word number 3
Word number 2 Word number 4
Word number 1 Word number X Word number 2 Word number Y"""

"""Task 3
Write a function called "choose_func" which takes a list of nums and 2 callback functions. 
If all nums inside the list are positive, execute the first function on that list and return the result of it. 
Otherwise, return the result of the second one"""
def choose_func(nums: list, func1, func2):
    if all(num > 0 for num in nums):
        result = func1(nums)
    else:
        result = func2(nums)
    return result

# Assertions
nums1 = [1, 2, 3, 4, 5, 6]
nums2 = [1, -2, 3, -4, 5, 7] 

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

#[1, 4, 9, 16, 25, 36]
#[1, 3, 5, 7]
