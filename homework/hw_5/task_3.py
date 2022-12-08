# Создайте программу для игры в ""Крестики-нолики""

import os
from  itertools import chain

def print_board(b):
    print('\n┌───┬───┬───┐')
    for i in range(len(b)):
        print(f'│ {b[i][0]} │ {b[i][1]} │ {b[i][2]} │')
        if i != len(b) - 1:
            print('├───┼───┼───┤')
    print('└───┴───┴───┘')

def player_switch(s):
    return 'O' if s == 'X' else 'X'

def winning_combination(b, mark):
    for row in range(len(b)):
        if b[row][0] == b[row][1] == b[row][2] == mark:
            return True
    for col in range(len(b)):
        if b[0][col] ==b[1][col] == b[2][col] == mark:
            return True
    if len(set([b[i][i] for i in range(len(b))])) == 1 and  b[0][0] == mark:
        return True
    if len(set([b[i][len(b) -1 -i] for i in range(len(b))])) == 1 and  b[0][2] == mark:
        return True
    return False

def board_filled(b):
    return ' ' not in chain(*b)

clear = lambda: os.system('cls')
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
play = True
player = 'O'

while play:
    player = player_switch(player)
    clear()
    print_board(board)
    print(f'Ход {player}')
    place = list(map(int, input('введите строку и столбец через запятую: ').split(',')))
    board[place[0]][place[1]] = player

    fill_check = board_filled(board)
    win_check = winning_combination(board, player)
    play = not(fill_check or win_check)

clear()
print_board(board)
if win_check:
    print(f'победитель {player}')
else:
    print('ничья')