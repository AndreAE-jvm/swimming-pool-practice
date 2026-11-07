# Задача 1. Реализуйте пузырьковую сортировку bubble_sort(lst).

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

print(bubble_sort([5, 1, 4, 2, 8]))  # [1, 2, 4, 5, 8]



# Задача 2. Реализуйте бинарный поиск binary_search(lst, target) (список отсортирован). Верните индекс или -1.

def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search([1, 3, 5, 7, 9], 7))  # 3


# Задача 3 (со звёздочкой). Реализуйте сортировку выбором selection_sort(lst) самостоятельно.
def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        # Ищем индекс минимального элемента в lst[i:]
        min_idx = i
        for j in range(i+1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        # Меняем местами текущий элемент и минимум
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

print(selection_sort([64, 25, 12, 22, 11]))  # [11, 12, 22, 25, 64]


# Задача 4 (со звёздочкой). Реализуйте binary_search_rec — бинарный поиск рекурсивно.

def binary_search_rec(lst, target, left=0, right=None):
    if right is None:
        right = len(lst) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if lst[mid] == target:
        return mid
    elif lst[mid] < target:
        return binary_search_rec(lst, target, mid + 1, right)
    else:
        return binary_search_rec(lst, target, left, mid - 1)

print(binary_search_rec([1, 3, 5, 7, 9], 7))  # 3
print(binary_search_rec([1, 3, 5, 7, 9], 4))  # -1