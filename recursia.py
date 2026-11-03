# Задача 1. Напишите рекурсивную функцию factorial(n).
# def factorial(n):
#     if n== 0 or n ==1:
#         return 1
#     return n * factorial(n-1)
#
# print(factorial(5))  # 120


# Задача 2. Напишите итеративную функцию fib_iter(n), возвращающую n-е число Фибоначчи.
# def fib_iter(n):
#     if n == 0:
#         return 0
#     a, b = 0, 1
#     for _ in range(n):   # сколько раз сдвинуться
#         a, b = b, a + b
#     return a
#
# print(fib_iter(10))  # 55


# Задача 3. Напишите рекурсивную функцию fib_rec(n).
# def fib_rec(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib_rec(n - 1) + fib_rec(n - 2)
#
# print(fib_rec(11))  # 55


# Задача 4 (со звёздочкой). Напишите рекурсивную функцию sum_digits(n), которая считает сумму цифр числа.
def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

print(sum_digits(1234))  # 10