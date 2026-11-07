
# Задача 1. Функция sum_from_file(filename) — читает файл с
# числами (по одному на строку) и возвращает сумму.

def sum_from_file(filename):
    total = 0
    with open(filename, "r") as f:
        for line in f:
            total += int(line.strip())
    return total

with open("numbers.txt", "w") as f:
    f.write("1\n2\n3\n4\n5\n")

print(sum_from_file("numbers.txt"))  # 15


# Задача 2. Функция filter_lines(input_file, output_file, keyword)
# — читает input_file, оставляет строки с keyword, записывает в output_file.


def filter_lines(input_file, output_file, keyword):
    with open(input_file, "r") as fin, open(output_file, "w") as fout:
        for line in fin:
            if keyword in line:
                fout.write(line)

with open("log.txt", "w") as f:
    f.write("INFO Started\nERROR Connection failed\nINFO Retry\nERROR Timeout\n")
filter_lines("log.txt", "errors.txt", "ERROR")
print(open("errors.txt").read())


# Задача 3 (со звёздочкой). count_words_in_file(filename)
# — возвращает словарь: слово → количество вхождений
# (без знаков препинания, регистр не важен).

def count_words_in_file(filename):
    result = {}
    # Таблица для удаления знаков препинания
    translator = str.maketrans('', '', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.lower().translate(translator)
            for word in line.split():
                result[word] = result.get(word, 0) + 1
    return result

# Создаём тестовый файл
with open("text.txt", "w", encoding="utf-8") as f:
    f.write("Hello, world! Hello Python.\nPython is great, isn't it?\n")

print(count_words_in_file("text.txt"))