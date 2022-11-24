# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

number = int(input('введите число n: '))
glos = {i : round((1 + 1 / i) **i, 2) for i in range(1, number+1)}
print(glos)
summa = 0
for i in glos.keys():
    summa += glos.get(i)
print(f'сумма: {summa}')