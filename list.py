def sum_list(lst):
    total = 0
    for x in lst:
        total += x
    return total
print(sum_list([1,2,3,4]))

def find_max(lst):
    max = lst[0]
    for x in lst:
        if x > max:
            max = x
    print(max)
find_max([3,7,2,8,1])

def reverse_list(lst):
    result = []
    for i in range(len(lst)-1,-1,-1):
        result.append(lst[i])
    print (result)
reverse_list([1,2,3])

def second_max(lst):
    result = sorted(set(lst))
    print(result[-2])
second_max([5,2,4,10,8])

