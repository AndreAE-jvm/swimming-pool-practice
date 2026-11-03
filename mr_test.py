def reverse_list(lst):
    result = []
    for i in range(len(lst)-1, -1, -1):
        result.append(lst[i])
    print(result)

reverse_list([1, 2, 3])  # [3, 2, 1]