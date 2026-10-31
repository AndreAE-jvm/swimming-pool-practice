def merge_dict(d1, d2):
    result = d1.copy()
    for key, value in d2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result
print(merge_dict({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))

def unique_words(text):
    clean = text.replace(",", "").replace(".","")
    result = set(clean.lower().split())
    return result
print(unique_words("the cat and the dog"))

def invert_dict(d):
    invert = {}
    for key, value in d.items():
        invert[value] = key
    return invert
print (invert_dict({'a':1, 'b':2, 'c':3}))




