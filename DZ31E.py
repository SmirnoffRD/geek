def my_round(number, ndigits):
#    x = str(number).find('.')
    lst = []
    for y in str(number): # y - элементы в числе
        lst.append(y)
    z = lst.index('.') # z - индексы в последовательности
    if int(lst[z + ndigits]) > 4:
        if lst[z + ndigits - 1] == ".":
            print(lst[z + ndigits - 1])
            n = int(lst[z + ndigits - 2]) + 1 # переменная для изменяемого элемента последовательности, не могли бы вы об.
            lst[z + ndigits - 2] = n
        else:
            n = int(lst[z + ndigits - 1]) + 1
            lst[z + ndigits - 1] = str(n)
    else:
        lst[z + ndigits] = 0
    k = z + ndigits # переменная для конца последовательности
    string = ''.join(lst[0:k])
    return string

res = my_round(2.1234567, 5)
print(res)


