# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности

from random import randint

def no_repeat_list(a):
    lst = []
    for i in a:
        if i not in lst:
            lst.append(i)
    return lst


rand_list = [randint(0, 20) for i in range(20)]
print(rand_list)
print(no_repeat_list(rand_list))