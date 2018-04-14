def My_filter(function, in_lst):
    new_lst = []

    for x in in_lst:
        if function(x):
            new_lst.append(x)
    return new_lst

ltc = [5, 4, 10, 12]    
f = lambda x: x % 3 == 0
print(My_filter(f, ltc))