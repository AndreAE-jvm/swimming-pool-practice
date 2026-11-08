# Задача 1. Напишите функцию, которая читает файл
# и возвращает количество строк в нём.

def count_lines(filename):
    total = 0
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            total += 1
    return total

print(count_lines("text.txt"))


# Задача 2. Напишите функцию, которая принимает список слов
# и возвращает словарь: первая буква → список слов.

def group_by_first_letter(words):
    result = {}
    for word in words:
        first = word[0]
        if first not in result:
            result[first] = []
        result[first].append(word)
    return result

print (group_by_first_letter(["apple", "banana", "avocado", "blueberry"]))
# {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry']}


# Задача 3. Реализуйте бинарный поиск в отсортированном списке (итеративно или рекурсивно — на ваш выбор).


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