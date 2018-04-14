def sort_to_max(origin_list):
    new_list = list.copy(origin_list)
    len_new = len(new_list)
    for _ in range(len_new):
        for x in range(len_new - 1):
            if new_list[x] > new_list[x + 1]:
                new_list[x], new_list[x + 1] = new_list[x + 1], new_list[x]
    
    return new_list







print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
