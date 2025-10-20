from asyncio import run_coroutine_threadsafe
from functools import partial

def multiply_two_numbers(a, b):
    print(a, b)
    return (a * b)

print(multiply_two_numbers(90,10))

multiply_numbers_by_two = partial(multiply_two_numbers,2)

print(multiply_numbers_by_two(9))

"""Example from lecture"""
import math
def make_cilinder_volume(r):
    def volume(h):
        print (f"r = {r},h = {h}, pi = {math.pi}")
        return   math.pi * r**2 * h
    return volume

volume_r10 = make_cilinder_volume(10)
print (volume_r10(12))

word = "Test"
command = "down"

def up(word):
    print(word.upper())

def down(word):
    print(word.lower())

def default(*args, **kwargs):
    print("Unknown command")

def process(command):
    command_dict = {
        "up" : up,
        "down" : down
    }
    if command in command_dict:
        return command_dict[command]
    else:
        return default

process('up')('Test1')
process('down')('shfyKJLJLKJLK')

"""Nested function"""
def test(word):
    print (f" word = {word}")
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
print(locals())

def make_multiplier(n):
  # Ця зовнішня функція повертає іншу функцію (множник)
  def multiplier(x):
    print(f"x = {x}, n = {n}")
    # Внутрішня функція використовує змінну 'n' із зовнішнього контексту
    return x * n
  return multiplier

# Створюємо функцію, яка множить на 2
double = make_multiplier(2)
# Створюємо функцію, яка множить на 3
triple = make_multiplier(3)

# Використовуємо створені функції
print(f"Double {double(13)}")  # Виведе 10
print(f"Triaple {triple(5)}")  # Виведе 15


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
