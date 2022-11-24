# Реализуйте алгоритм перемешивания списка.
from random import randint

user_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
print(f'первоначальный список:\t{user_list}')
lenght = len(user_list)
count = lenght * 20     # чтобы перемешивало и на больших списках 
while count > 0:
    a = randint(0, lenght-1)
    b = randint(0, lenght-1)
    user_list[a], user_list[b] = user_list[b], user_list[a]
    count -= 1
print(f'перемешанный список:\t{user_list}')
