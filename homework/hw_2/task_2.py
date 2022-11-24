# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def factorial(num):
    result = 1
    while num > 0:
        result *= num
        num -= 1
    return result

number = int(input('введите число N: '))
list_of_factorials = [factorial(i) for i in range(1, number)]
print(list_of_factorials)