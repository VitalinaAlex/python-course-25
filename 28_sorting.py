import time
import random

"""
Task 1
A bubble sort can be modified to "bubble" in both directions. The first pass moves "up" the list and the second pass moves "down."
This alternating pattern continues until no more passes are necessary. 
Implement this variation and describe under what circumstances it might be appropriate.""" 

# Реалізації сортувань з попередніх прикладів

def cocktail_shaker_sort(arr, _is_recursive=False):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start += 1
    return arr

"""
Task 2. Implement the mergeSort function without using the slice operator."""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

"""
Task 3. One way to improve the quicksort is to use an insertion sort on lists that are small in length (call it the "partition limit"). 
Why does this make sense? Re-implement the quicksort and use it to sort a random list of integers. 
Perform analysis using different list sizes for the partition limit."""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def quick_sort(arr, limit=10):
    if len(arr) <= limit:
        return insertion_sort(arr)

    element = arr[len(arr) // 2]
    left = [x for x in arr if x < element]
    middle = [x for x in arr if x == element]
    right = [x for x in arr if x > element]

    return quick_sort(left, limit) + middle + quick_sort(right, limit)

list_size = 77
random_list = [random.randint(0, 10000) for _ in range(list_size)]
print("Вихідний список:", random_list)

arr1 = random_list.copy()
arr2 = random_list.copy()
arr3 = random_list.copy()
limit = round(list_size * 0.02) 
# зазвичай беруть 1-5% від розміру списку. 
# чим менший ліміт, тим більше рекурсійних викликів буде зроблено, тим більше часу займе сортування. 


start_snaker = time.time()
cocktail_shaker_sort(arr1)
end_snaker = time.time()
print(f"⏱ shaker_sort виконано за {end_snaker - start_snaker:.6f} секунд")
print("Відсортований список (shaker_sort):", arr1)
start_sorted = time.time()
sorted_merge = merge_sort(arr2)
end_sorted = time.time()
print(f"⏱ merge_sort виконано за {end_sorted - start_sorted:.6f} секунд")
print("Відсортований список ( merge_sort):", sorted_merge)
quick_sort(arr3, limit=limit)
start_quick = time.time()
sorted_quick = quick_sort(arr3, limit=limit)
end_quick = time.time()
print(f"⏱ quick_sort виконано за {end_quick - start_quick:.6f} секунд")
print("Відсортований список ( quick_sort):", sorted_quick)
result = min(end_snaker - start_snaker, end_sorted - start_sorted, end_quick - start_quick)
print(f'⏱ {result:.6f} секунд - найшвидший час сортування серед трьох алгоритмів.')


def timed_sort(func, arr, **kwargs):
    start = time.time()
    result = func(arr.copy(), **kwargs)
    end = time.time()
    elapsed = end - start
    return result, elapsed

test_cases = {
    "Випадковий список": [random.randint(0, 100) for _ in range(20)],
    "Вже відсортований": list(range(20)),
    "Зворотний порядок": list(range(20, 0, -1)),
    "Однакові елементи": [5] * 20,
    "Частково відсортований": [1,2,3,15,14,13,4,5,6,20,19,18,7,8,9,10,12,11,16,17]
}

# Тестові дані для аналізу роботи різних списків
for name, arr in test_cases.items():
    print(f"\n=== Тест: {name} ===")
    
    shaker_sorted, shaker_time = timed_sort(cocktail_shaker_sort, arr)
    merge_sorted, merge_time = timed_sort(merge_sort, arr)
    quick_sorted, quick_time = timed_sort(quick_sort, arr, limit=5)
    
    print(f"cocktail_shaker_sort: {shaker_sorted} (час: {shaker_time:.6f} сек)")
    print(f"merge_sort:           {merge_sorted} (час: {merge_time:.6f} сек)")
    print(f"quick_sort:           {quick_sorted} (час: {quick_time:.6f} сек)")
    
    
    if shaker_sorted == merge_sorted == quick_sorted:
        print("✅ Всі три функції повернули однаковий результат")
    else:
        print("❌ Результати відрізняються")
    
    # хто кращий у цьому типі списку
    times = {
        "cocktail_shaker_sort": shaker_time,
        "merge_sort": merge_time,
        "quick_sort": quick_time
    }
    fastest = min(times, key=times.get)
    slowest = max(times, key=times.get)
    
    print(f"⏱ Найшвидша функція: {fastest} ({times[fastest]:.6f} сек)")
    print(f"⏱ Найповільніша функція: {slowest} ({times[slowest]:.6f} сек)")