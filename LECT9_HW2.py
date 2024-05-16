def linearize_list(lst):
    flat_lst = []
    flatter_lst = []
    for element in lst:
        if type(element) is list:
            for item in element:
                flat_lst.append(item)
        else:
            flat_lst.append(element)
    for element in flat_lst:
        if type(element) is list:
            for item in element:
                flat_lst.append(item)
        else:
            flatter_lst.append(element)
    return sorted(flatter_lst)


lst = [1, 2, [3, 4, [5, 6], 7], 8, [9, [10]], 11]
# lst = [[1, [2], 3, 4], [5, [1, 6, 7], 7], [8, 9, 10]]
# lst = [12, 11, [[10], 9], 8, [7, [5, 6], 1], 0]

print(linearize_list(lst))
