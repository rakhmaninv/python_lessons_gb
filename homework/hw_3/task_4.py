# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

num = int(input('введите число: '))
# num_bin = bin(num)
# print(num_bin[2:])

# print('{0:b}'.format(num))

num_bin = []
i = num 
while i != 0:
    num_bin.insert(0, str(i % 2))
    i = i // 2
print(''.join(num_bin))