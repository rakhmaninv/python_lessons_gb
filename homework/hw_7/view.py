
def user_input(msg):
    return input(f'{msg}: ')

def get_file_extention():
    print('выберите расширение')
    extention = input('1-txt, 2-csv  ')
    if extention is '1':
        return 'txt'
    else:
        return 'csv'

def contact_input():
    print('введите фамилию, имя, телефон и описание через пробел')
    return input().split()
