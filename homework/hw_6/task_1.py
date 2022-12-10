from random import randint
def task_1():
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
    print(sum([int(i) for i in input('введите вещественное число: ') if i.isdigit()]))

def task_2():
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
    lst = [randint(1, 5) for i in range(10)]
    print(sum([value for index, value in enumerate(lst) if not(index % 2)]))

def task_3():
# Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
    coin = 'OOOPPOPOOOPPPPPOPPPPPPOOPPP'
    lst = list(filter(None, coin.split('O')))
    print(max(list(map(lambda x: len(x), lst))))

def task_4():
# Дан список, вывести отдельно буквы и цифры.
    a = ['a', 'b', '2', '3' ,'c']
    b_lst = list()
    c_lst = list()
    for i in a:
        (lambda x, b, c: b.append(x) if x.isdigit() else c.append(x))(i, b_lst, c_lst)
    print(b_lst, c_lst)
