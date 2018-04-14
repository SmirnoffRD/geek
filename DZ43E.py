# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random
new_numbers = []
numbers = [random.randint(-10, 10) for _ in range(10)]
print(numbers)
# for x in numbers:
new_numbers += filter(lambda x: x % 3 == 0, 
filter(lambda n: n % 4 != 0, 
filter(lambda y: y > 0, numbers)))
print(new_numbers)
