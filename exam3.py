# Задача 1. Напишите функцию, которая читает CSV-файл и возвращает список словарей (каждая строка — словарь).
def read_csv(filename):
    result = []
    with open(filename, "r", encoding="utf-8-sig") as f:
        headers = f.readline().strip().split(",")
        for line in f:
            values = line.strip().split(",")
            row = {}
            for i in range(len(headers)):
                row[headers[i]] = values[i]
            result.append(row)
    return result

print(read_csv("students.csv"))


# [{'name': 'Alice', 'grade': '5'}, {'name': 'Bob', 'grade': '3'}, ...]

# Задача 2. Напишите функцию, которая принимает текст и возвращает список слов, отсортированных по длине (от коротких к длинным).
def sort_words_by_length(text):
    words = text.split()
    return sorted(words, key=len)

print(sort_words_by_length("привет мир как дела"))
# ['как', 'мир', 'дела', 'привет']


# Задача 3. Реализуйте класс Stack с
# методами push, pop, peek, is_empty.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

s = Stack()
s.push(1)
s.push(2)
print(s.pop())      # 2
print(s.peek())     # 1
print(s.is_empty()) # False

