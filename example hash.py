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