# Напишите программу, которая по заданному номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).

while True:
    try:
        quarter = int(input('введите номер четверти (1, 2, 3 или 4)'))
        if quarter in range(1, 5):
            break
    except ValueError:
        print('введите целое число')

if quarter == 1:
    print('x(0, ∞) y(0, ∞)')
elif quarter == 2:
    print('x(0, -∞) y(0, ∞)')
elif quarter == 3:
    print('x(0, -∞) y(0, -∞)')
else:
    print('x(0, ∞) y(0, -∞)')