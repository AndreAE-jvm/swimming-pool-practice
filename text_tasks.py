# Задача 1. split_sentences(text) — разбивает текст на предложения (по ., !, ?).


import re

def split_sentences(text):
    sentences = re.split(r'[.!?]+', text)
    return [s.strip() for s in sentences if s.strip()]

print(split_sentences("Привет. Как дела? Хорошо!"))  # ['Привет', 'Как дела', 'Хорошо']

# Задача 2. longest_word_per_sentence(text) —
# список самых длинных слов в каждом предложении.

def longest_word_per_sentence(text):
    result = []
    for sentence in split_sentences(text):
        words = sentence.split()
        if words:
            longest = max(words, key=len)
            result.append(longest)
    return result

print(longest_word_per_sentence("Привет мир. Как дела?"))  # ['Привет', 'дела']

# Задача 3 (со звёздочкой).
# word_frequency(text) — список кортежей (слово, частота),
# отсортированный по убыванию частоты.


def word_frequency(text):
    # Приводим к нижнему регистру и убираем знаки препинания
    text = text.lower()
    for p in '.,!?;:()[]{}"\'—–-':
        text = text.replace(p, " ")
    # Разбиваем на слова
    words = text.split()
    # Считаем частоту
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    # Сортируем по убыванию частоты
    result = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return result

print(word_frequency("Привет мир! Привет Python. Мир прекрасен."))
# [('привет', 2), ('мир', 2), ('python', 1), ('прекрасен', 1)]