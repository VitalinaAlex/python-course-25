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