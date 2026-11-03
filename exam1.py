# Напишите функцию, которая принимает список чисел и возвращает список только чётных чисел.
# def list_even(lst):
#     result = []
#     for x in lst:
#         if x % 2 == 0:
#             result.append(x)
#     return result
# lst = [1,2,3,4,5,6,7,8,9,10]
# print(list_even(lst))

# def lst_even(lst):
#     even = [x for x in lst if x % 2 == 0]
#     return even
# lst = [1,2,3,4,5,6,7,8,9,10]
# print(lst_even(lst))





# Напишите функцию, которая принимает строку и возвращает словарь: слово → его длина.
# def str_dict(s):
#     dct = {}
#     r = s.split()
#     for word in r:
#         dct[word] = len(word)
#     return dct
#
# row = ('А роза упала на лапу Азора')
# print(str_dict(row))




# Напишите рекурсивную функцию для вычисления суммы чисел от 1 до n.
def sum_to(n):
    if n <= 0:
        return 0
    return n + sum_to(n - 1)

print(sum_to(3))