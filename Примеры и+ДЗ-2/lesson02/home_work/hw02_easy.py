# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
# spisok = ["яблоко", "банан", "киви", "арбуз"]

# k = 0
# for i in spisok:
#     i = str(k + 1) + " " + i
#     spisok[k] = i
#     k += 1
# print(spisok)

# k = 1
# for i in spisok:
#     i = str(k) + ' ' + i
#     k += 1
#     print(i)
# gm = 0
# for g in spisok:
#     if int(len(g)) > gm:
#         gm = len(g)
# k = 0
# # print(gm)
# for s in spisok:
#     k += 1
# #    print(s)
#     print(str(k) + '.' + str(" " * (1 + gm - len(s))) + s)

#Second variant
# fruits = ['apple', 'banana', 'kiwi', 'watermelon']
# align_step = len(max(fruits, key=len))
# print(align_step)
# for index, item in enumerate(fruits, start=1):
#     print("{}. {:>{}}".format(   # :> выравниваем в правый край, а далее на сколько символов.
#         index, item, align_step
#     ))
    


# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
# spisok = ["яблоко", "банан", "киви", "арбуз", "apteka", "ylitca"]
# spi = ["яблоко", "банан", "киви", "арбуз"]

# for x in spi:
#     if x in spisok:
#         spisok.remove(x)
# print(spisok)
    
            
# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
first = [4, 8, 15, 16, 23, 42]
second = []
for y in first:
    if y % 2 == 0:
        second.append(y / 4)
    else:
        second.append(y * 2)
print(second)









