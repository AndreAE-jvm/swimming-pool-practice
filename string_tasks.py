def is_palindrome(s):
    s = s.lower().replace(" ","")
    return s == s[::-1]
print (is_palindrome("А роза упала на лапу Азора"))

def count_vowels(s):
    s = s.lower()
    cnt_vowels = 0
    for char in s:
        if char in "аеёиоуыэюяaeiou":
            cnt_vowels += 1
    return cnt_vowels
row1 = count_vowels("привет")
row2 = count_vowels("hellowou")
print(f"Количество гласных русских букв равно {row1}\n")
print(f"Количество гласных английских букв равно {row2}\n")

def capitalize_words(s):
    words = s.split()
    result = []
    for word in words:
        result.append(word[0].upper() + word[1:])
    return " ". join(result)
print(capitalize_words("hellow world schole 21"))


def remove_duplicates(s):
    seen = set()
    result = []
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    return "".join(result)

print(remove_duplicates("abacabad"))


