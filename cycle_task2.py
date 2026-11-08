def second_max(lst):
    result = sorted(set(lst))
    print(result[-2])
second_max([5,2,4,10,8])