# def find_max(lst):
#     max_val = 0
#     for x in lst:
#         if x > max_val:
#             max_val = x
#     return max_val
#
# print(find_max([-5, -2, -10]))  # ожидается -2, но что выведет?
#
#
# def find_max(lst):
#     max_val = float('-inf')
#     for x in lst:
#         if x > max_val:
#             max_val = x
#     return max_val
#
# print(find_max([-5, -2, -10]))  # -2



# «Напиши функцию на Python, которая проверяет, является ли строка аннаграммой другой строки.»

def is_anagram(s1, s2):
    # Приводим к нижнему регистру и убираем пробелы
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    # Сравниваем отсортированные строки
    return sorted(s1) == sorted(s2)

print(is_anagram("", ""))              # True
print(is_anagram("Listen", "Silent"))  # True
print(is_anagram("a b", "ab"))         # True (если пробелы игнорируются)
print(is_anagram("abc", "ab"))         # False