# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.

def user_input_int_number(msg):
    while True:
        try:
            number = int(input(msg))
            return number
        except ValueError:
            print('введите целое число') 

week_range = range(1,8)
while True:
    day_number = user_input_int_number('введите число дня недели (1-понедельник, 2-вторник, и т.д.): ')
    if day_number in week_range:
        break
    else:
        print('неправильное число')

if day_number >= 6:
    print('ваш день выходной')
else:
    print('ваш день будний')