# Создать текстовый файл, записать в него построчно данные, которые вводит пользователь. 
# Окончанием ввода пусть служит пустая строка.
def t1():
    path = 'C:\\Users\\user\\Documents\\gb\\Python_lessons\\seminars\\test.txt'
    with open(path, 'a') as data:
        while True:
            user_str = input()
            if user_str == '':
                break
            data.write(user_str + '\n')

def t2():
    data = open('file.txt', 'r', encoding='UTF-8')
    for s in data.readlines():
        print(s, end='')
        print(f'Количество символов = {len(s)}')
        print(f"Количество слов = {len(s.split())}")
        print()
    data.close()

def t3():
    string = '1 2 3 4 5'
    string = string.split()
    count = 0
    for i in range(1, len(string)):
        if string[i] > string[i - 1]:
            count += 1
    print(count)