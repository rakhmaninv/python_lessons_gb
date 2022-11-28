# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем 
# первый и последний элемент, второй и предпоследний и т.д.

from random import randint
def pair_multiplication_list(lst):
    return [lst[i] * lst[-1 - i] for i in range(round(len(lst) / 2))]

rand_list = [randint(1, 9) for i in range(int(input('введите длину списка: ')))]
print(rand_list)

pair_list = pair_multiplication_list(rand_list)
print(pair_list)