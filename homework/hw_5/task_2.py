# Создайте программу для игры с конфетами человек против человека.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
from random import randint

def take_candies_user(limit):
    while True:
        user_take = int(input('сколько взять конфет?: '))
        if 0 < user_take < (limit + 1):
            return user_take
        print(f'можно взять от 1 до {limit} конфет')

def player_switch(player):
    return 1 if player == 0 else 0

def difficulty_select(x):
    if x == '3':
        return [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    elif x == '2':
        return [0, 0, 0, 0, 0, 1, 1, 2, 3, 5]
    else:
        return [0, 0, 1, 2, 4, 5, 6, 8, 11, 15]

candies = 120
take_limit = 28
game = input('игра против 1-игрока или 2-бота: ')
if game == '2':
    difficulty = difficulty_select(input('сложность: 1-легко, 2-средне, 3-тяжело: '))
player = randint(0, 1)
while candies > 0:
    player = player_switch(player)
    print(f'Игрок: {player +1}    Конфет: {candies}')
    if player == 0:
        candies -= take_candies_user(take_limit)
    else:
        if game == '1':
            candies -= take_candies_user(take_limit)
        else:
            bot_take = (lambda x, y, lst: x % (y +1 -lst[randint(0, 9)]))(candies, take_limit, difficulty)
            candies -= bot_take
            print(f'бот взял {bot_take} конвет')
if game == '1':
    print(f'победил игрок {player +1}')
else:
    if player == 0:
        print('победил игрок')
    else:
        print('победил бот')


