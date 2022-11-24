# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение 
# элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
from random import randint

num = int(input('введите число N: '))
lst = [randint(-num, num) for i in range(num)]
print('список:')
print(lst)

result = 1
filename = 'C:\\Users\\user\\Documents\\gb\\Python_lessons\\homework\\hw_2\\file.txt'

with open(filename) as pos:
    content =  pos.read().split()
    print('позиции: ', *content)
    for i in content:  
        result *= lst[int(i)-1]
pos.close
print(f'произведение элементов: {result}')