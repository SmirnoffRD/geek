
__author__ = 'Ваши Ф.И.О.'

# Задача-1: Дано произвольное целое число, вывести поочередно цифры исходного числа

# код пишем тут...
number = input('Vvedite chislo: ')
dlina = len(number)

for x in number:
    print(x)
    
# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!
a = input()
b = input()
c = a
a = b
b = c
print(a)
print(b)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
vozrast = int(input('Vvedite vozrast: '))
D = 'A'
while D != 'Q':
    if vozrast >= 18:
        print("Dostyp razreshen")
        break
    else:
        print("Pshel nahyu pizduk")
    D = input("Popitautes snova[Y/Q]: ")
    vozrast = int(input('Vvedite vozrast: '))    