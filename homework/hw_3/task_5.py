# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def negafibonacci(n):
    if n == 1 or n == -1:
        return 1
    elif n == 0:
        return 0
    elif n < 0:
        return negafibonacci(n + 2) - negafibonacci(n + 1)
    else:
        return negafibonacci(n - 1) + negafibonacci(n - 2)

num = int(input('введите число: '))
lst = []
for i in range(num + 1):
    lst.append(negafibonacci(i))
    if i != 0:
        lst.insert(0, negafibonacci(-i))
print(lst)