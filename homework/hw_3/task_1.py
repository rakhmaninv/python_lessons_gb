# Задайте список из нескольких чисел. Напишите программу, которая найдёт 
# сумму элементов списка, стоящих на нечётной позиции.

from random import randint

lst = [randint(1, 99) for i in range(int(input('введите длину списка: ')))]
print(lst)

sum_of_odd = sum(lst[i] for i in range(1, len(lst), 2))
print(f'сумма: {sum_of_odd}')
