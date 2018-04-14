import random

numbers_list = [random.randint(-10, 10) for _ in range(10)]



print(numbers_list)

new_list = []
new_list = list(map(lambda x: x**2, numbers_list))

print(new_list)




