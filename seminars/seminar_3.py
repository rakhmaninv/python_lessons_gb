def t1():
    # Орел и решка
    # Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки. Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
    # Формат входных данных
    # На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".
    # Формат выходных данных
    # Программа должна вывести наибольшее количество подряд выпавших Решек.
    # Примечание. Если выпавших Решек нет, то необходимо вывести число 0


    str_money = input('Введи строку ')
    count_max = 0
    count = 0

    for i in range(len(str_money)):
        if str_money[i] == 'Р':
            count += 1
        if count > count_max:
            count_max = count
        if str_money[i] == 'О':
            count = 0
    print(count_max)


# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. 
# Теперь он использует их в качестве серверов "Пегого дудочника". Помогите владельцу фирмы 
# отыскать все зараженные холодильники.Для каждого холодильника существует строка 
# с данными, состоящая из строчных букв и цифр, и если в ней присутствует слово "anton" 
# (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен 
# и нужно вывести номер холодильника, нумерация начинается с единицы
# Формат входных данных
# В первой строке подаётся число 
# n
# n – количество холодильников. В последующих 
# n
# n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 
# 5
# 5 до 
# 100
# 100 символов.

# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел. Если таких 
# холодильников нет, ничего выводить не нужно.

# num = int(input('количество холодильников: '))
# for i in range(num):

# name = 'a1n1t1o1n1'
# ai_name = 'anton'
# for i in name:
#     if i in ai_name:
#         name[i].pop


number_holodos = int(input('Введи число '))
list_holodos = []

counter = 0
for i in range(number_holodos):
    row = input('Введи строку ')
    list_holodos.append(row)
    print(row.index('a'))
    if ('a' in row):
        counter += 1
        if ('n' in row):
            counter += 1
            if ('t' in row):
                counter += 1
                if ('o' in row):
                    counter += 1
                    if ('n' in row):
                        counter += 1
                        if counter == 5:
                            break
                            


