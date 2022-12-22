import view as v
import model as m


def start():
    data = m.get_data()
    keys = list(data[0].keys())

    run = True
    while run == True:
        match v.show_menu():
            case 1: # find employee
                v.print_employee_table(m.employee_search(data, v.search_parameters(keys)))

            case 2: #emloyees by title
                v.print_employee_table(m.job_title_selection(data, v.job_tittle_choice(data)))

            case 3: #emloyees by salary
                v.print_employee_table(m.salary_selection(data, v.salary_range_input()))

            case 4: #add employee
                m.add_employee(data, keys, v.user_input('введите имя, фамилию, должность и зарплату через пробел: '))

            case 5: #delete employee
                v.print_employee_table(data)
                data = m.delete_employee(data, v.user_input('введите id сотрудника, которого хотите удалить: '))

            case 6: #update employee
                v.print_employee_table(data)
                m.update_eployee(data, 
                                v.user_input('введите id сотрудника, данные которого хотите обновить: '),
                                v.search_parameters(keys, update=True))

            case 7: #export json
                m.export_to_json(data, keys, v.user_input('введите имя файла'))

            case 8: #export csv
                m.save_data_csv(data, keys, v.user_input('введите имя файла'))

            case 9: #close
                run = False
        input('\n' + '---нажмите Enter для продолжения---')
    m.save_data_csv(data, keys)
