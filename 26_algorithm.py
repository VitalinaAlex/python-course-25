"""Програма мінімум:
Реалізувати алгоритм бінарного пошуку за допомогою рекурсії.
Прочитати про Fibonacci search та імплементуйте його за допомогою Python. 
Визначте складність алгоритму та порівняйте його з бінарним пошуком"""

def binary_search(arr, target, low, high):
    if low > high:
        return False  # Елемент не знайдено

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1) 

my_list = []
n = 10
for i in range(0, n+1):
    my_list.append(i*2)
result = binary_search(my_list, 11, 0, n)
print(result)
print(my_list) 

"""Середній рівень:
Реалізувати in (__contains__) та len (__len__) методи для HashTable"""