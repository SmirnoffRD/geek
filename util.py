# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"


import easy
print("Hello user")
while True:
    print('What do you want?\n 1. Change wdir\n 2. View on list of files and dir\n 3. Dell dir\n 4. Create dir\n 5. Exit')
    variant = input(':', )
    if variant == '1':
        easy.change_dir()
    elif variant == '2':
        easy.list_of_files()
    elif variant == '3':
        easy.del_dir()
    elif variant == '4':
        easy.cr_dir()
    elif variant == '5':
        print('Drink only "Kaluga beer" Goodbuy!')
        break
