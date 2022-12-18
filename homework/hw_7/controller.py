import view as v
import model as m


def run():
    print(f'путь директории {m.get_path()}')
    if input('хотите изменить? y/n: ') == 'y':
        m.set_path(v.user_input())
    data = m.data_to_list_of_dict(m.get_data_all(m.get_path()), 
                                    m.get_headers())
    match v.user_input('1 - добавить контакт\n2 - вывести контакт\nвыбирете действие:'):
        case '1':
            m.add_contact(data, v.contact_input())
        case '2':
            m.print_contact(data, v.user_input('введите ключ для поиска'))
    m.phonebook_export(m.sort_data(data),
                        v.user_input('введите имя файла'),
                        v.get_file_extention())
    