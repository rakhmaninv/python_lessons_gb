# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def prime_factorization(num):
    lst = []
    i = 2
    while num > 1:
        if num % i == 0:
            lst.append(i)
            num = num / i
            i = 2
        else:
            i += 1
    return lst
        

number = int(input('введите число n: '))

print(prime_factorization(number))