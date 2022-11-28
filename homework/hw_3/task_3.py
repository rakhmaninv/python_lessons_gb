# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.

import random

lst = [round(random.uniform(0.00, 9.99), 2) for i in range(6)]
print(lst)

min_float = max_float = lst[0] % 1
for i in lst:
    if i % 1 < min_float:
        min_float = i % 1
    if i % 1> max_float:
        max_float = i % 1

print(f'разница: {round(max_float - min_float, 2)}')
