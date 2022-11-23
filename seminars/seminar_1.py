def user_input_int_number(msg):
    while True:
        try:
            number = int(input(msg))
            return number
        except ValueError:
            print('введите целое число') 
def user_input_float_number(msg):
    while True:
        try:
            number = float(input(msg))
            return number
        except ValueError:
            print('введите дробное число') 
def t1():
#  Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
    num_n = user_input_int_number('введите число N: ')
    lst = []
    for i in range(-num_n, num_n+1):
        lst.append(i)
    print(*lst)

def t2():
# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    num_float = user_input_float_number('введите дробное число')
    print(int(num_float*10)%10)

def t3():
#Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
    num_check = user_input_int_number('введите целое число: ')
    if (num_check % 5 == 0 and num_check % 10 == 0 or num_check % 15 == 0) and num_check % 30 != 0:
        print(True)
    else:
        print(False)
t3()