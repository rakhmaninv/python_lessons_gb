# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint, sample

number = int(input('введите степень: '))
coefficients = [randint(0, 100) for _ in range(number + 1)]
powers = [f'*x^{i}'if i > 1 else '*x' for i in range(number, 0, -1)]
terms = [str(a) + str(b) for a, b in zip(coefficients, powers + [''])]

with open('homework\\hw_4\\4_polynomial_w.txt', 'w') as data:
    data.write(' + '.join(terms) + ' = 0')
    