# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
# выдаёт номер четверти плоскости, в которой находится эта точка .

while True:
    x_coord, y_coord = map(int, input('введите координаты точки через ,: ').split(', '))
    if x_coord != 0 and y_coord != 0:
        break
    print('точка не должна находится на оси')

if x_coord > 0 and y_coord > 0:
    print('точка находится в 1 четверти')
elif x_coord < 0 and y_coord > 0:
    print('точка находится в 2 четверти')
elif x_coord < 0 and y_coord < 0:
    print('точка находится в 3 четверти')
else:
    print('точка находится в 4 четверти')