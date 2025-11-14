"""Програма мінімум:
Реалізувати алгоритм бінарного пошуку за допомогою рекурсії.
Прочитати про Fibonacci search та імплементуйте його за допомогою Python. 
Визначте складність алгоритму та порівняйте його з бінарним пошуком"""
import time

def binary_search(arr, target, low, high):
    if low > high:
        return -1  # Елемент не знайдено

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1) 

my_list = []
max_value = len(my_list)-1
min_value = 0
find = 11
for i in range(min_value, 12):
    my_list.append(i*2)
start = time.time()
result1 = binary_search(my_list, find, min_value, len(my_list)-1)
end = time.time()
print(f"Пошукове число {find} має індекс {result1} у наявному рядку:")
print(my_list)
print(f"Час виконання: {end - start:.10f} секунд")


my_list = []
max_value = 10
min_value = -2
find = 18
for i in range(min_value, max_value+1):
    my_list.append(i*2)
start = time.time()
result2 = binary_search(my_list, find, min_value, len(my_list)-1)
end = time.time()
print(f"Пошукове число {find} має індекс {result2} у наявному рядку:")
print(my_list)
print(f"Час виконання: {end - start:.10f} секунд")

"""Середній рівень:
Реалізувати in (__contains__) та len (__len__) методи для HashTable"""
def fibonacci_search(arr, target):
    fibM2 = 0  # (m-2)'th Fibonacci No.
    fibM1 = 1  # (m-1)'th Fibonacci No.
    fibM = fibM2 + fibM1  # m'th Fibonacci

    n = len(arr)

    while (fibM < n):
        fibM2 = fibM1
        fibM1 = fibM
        fibM = fibM2 + fibM1

    offset = -1

    while (fibM > 1):
        i = min(offset + fibM2, n - 1)

        if (arr[i] < target):
            fibM = fibM1
            fibM1 = fibM2
            fibM2 = fibM - fibM1
            offset = i

        elif (arr[i] > target):
            fibM = fibM2
            fibM1 = fibM1 - fibM2
            fibM2 = fibM - fibM1

        else:
            return i

    if(fibM1 and offset + 1 < n and arr[offset + 1] == target):
        return offset + 1

    return "Елемент не знайдено"
my_list = []
find = 18
for i in range(-2, 11):
    my_list.append(i*2)
start = time.time()
result3 = fibonacci_search(my_list, find)
end = time.time()
print(f"Пошукове число {find} має індекс {result3} у наявному рядку:")
print(my_list)
print(f"Час виконання: {end - start:.10f} секунд")

class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size

    def __setitem__(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
        self.count += 1

    def __getitem__(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        raise KeyError(f'Key {key} not found.')

    def __contains__(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return True
        return False

    def __len__(self):
        return self.count
    def __repr__(self):
        items = []
        for bucket in self.table:
            for k, v in bucket:
                items.append(f"{k}: {v}")
        return "{" + ", ".join(items) + "}"

hash_table = HashTable()
hash_table["apple"] = 1
hash_table["banana"] = 2
hash_table["orange"] = 3
print(hash_table)
print("banana" in hash_table)  # Виведе: True
print("grape" in hash_table)   # Виведе: False
print(f"Length hash_table {len(hash_table)}")         # Виведе: 3  

list_items = [("apple_list", 1), ("banana_list", 2), ("orange_list", 3)]
for key, value in list_items:
    hash_table[key] = value
print(f"Length list {len(list_items)}")  # Виведе: 3
print(hash_table["orange"])  # Виведе: 3
print(f"Length hash_table {len(hash_table)}")
print(hash_table)

list2_items = [("apple2_list", 4), ("banana2_list", 5), ("orange2_list", 6)]
for key, value in list2_items:
    hash_table[key] = value
print(len(list2_items))  # Виведе: 3
print(hash_table["orange"])  # Виведе: 3
print(f"Length hash_table {len(hash_table)}")
print(hash_table)

import unittest
print(f"{'-'*5}Тести для HashTable{'-'*5}")
class TestHashTable(unittest.TestCase):

    def setUp(self):
        """Готуємо хеш-таблицю перед кожним тестом"""
        self.hash_table = HashTable()
        self.hash_table["apple"] = 1
        self.hash_table["banana"] = 2
        self.hash_table["orange"] = 3

    def test_initial_insert(self):
        self.assertEqual(self.hash_table["apple"], 1)
        self.assertEqual(self.hash_table["banana"], 2)
        self.assertEqual(self.hash_table["orange"], 3)
        self.assertEqual(len(self.hash_table), 3)

    def test_check_existence(self):
        self.assertTrue("banana" in self.hash_table)
        self.assertFalse("grape" in self.hash_table)

    def test_insert_list_items(self):
        list_items = [("apple_list", 1), ("banana_list", 2), ("orange_list", 3)]
        for key, value in list_items:
            self.hash_table[key] = value

        self.assertEqual(len(self.hash_table), 6)  # 3 старих + 3 нових
        self.assertEqual(self.hash_table["orange"], 3)

    def test_insert_second_list(self):
        list2_items = [("apple2_list", 4), ("banana2_list", 5), ("orange2_list", 6)]
        for key, value in list2_items:
            self.hash_table[key] = value

        self.assertEqual(len(self.hash_table), 6)  # Перевірка після нових вставок
        self.assertEqual(self.hash_table["banana"], 2)
        self.assertEqual(self.hash_table["orange"], 3)

if __name__ == "__main__":
    unittest.main()