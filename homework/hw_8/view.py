from tabulate import tabulate


def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))

def user_input(msg):
    return input(f'{msg}: ')

def search_parameters(key, update= False):
    msg = 'обновления' if update == True else 'поиска' 
    print("\n" + "=" * 20)
    for count, value in enumerate(key):
        print(count, value)
    k = list(map(int, input(f'введите номер поля для {msg}(несколько через пробел): ').split()))
    v = input(f'введите параметры для поиска(несколько через пробел): ').split()
    return dict(zip([key[i] for i in k], v))

def print_employee_table(data):
    print("\n")
    print(tabulate(data, headers='keys', floatfmt=".2f"))

def job_tittle_choice(data):
    print("\n" + "=" * 20)
    job_values = list(set(i['job_title'] for i in data))
    for count, value in enumerate(job_values):
        print(count, value)
    return job_values[int(input('введите номер должности для выборки: '))]
    
def salary_range_input():
    print("\n" + "=" * 20)
    return tuple(map(float, input('введите мин и макс зарплату через пробел: ').split()))
        

