# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number_str = input('введите вещественное число: ')
digits = ['0','1','2','3','4','5','6','7','8','9']
sum_of_digits = 0
for i in number_str:
    if i in digits:
        sum_of_digits += int(i)
print(f'сумма цифр: {sum_of_digits}')