from os import listdir


path = 'homework\hw_7\data\\'
headers = ['last_name', 'first_name', 'phone_number', 'discription']

def get_data_all(path):
    data = str()
    for i in listdir(path):
        with open(path + i, 'r', encoding='utf-8-sig') as f:
            data += f.read() + '\n'
    return data

def print_contact(data, contact):
    for i in data:
        if contact in i:
            print(i)

def phonebook_export(data, name, ext):
    new_file = f'{get_path()}{name}.{ext}'
    with open(new_file , 'w', encoding='utf-8-sig') as f:
        for i in range(len(data)):
            f.write(','.join(data[i].values()))
            if i != len(data) -1:
                f.write('\n')

def data_to_list_of_dict(data, keys):
    lst = [row.split(',') for row in list(filter(None, data.split('\n')))]
    return [dict(zip(keys, values)) for values in lst]

def add_contact(data, contact):
    headers = get_headers()
    contact_dict = {headers[i]: contact[i] for i in range(len(headers))}
    data.append(contact_dict)

def sort_data(data):
    no_duplicates = list(map(dict, set(tuple(i.items()) for i in data)))
    return sorted(data, key=lambda x: x[next(iter(no_duplicates[0]))])

def get_headers():
    global headers
    return headers

def get_path():
    global path
    return path

def set_path(user_path: str):
    global path
    if not user_path.endswith('\\'):
        user_path += '\\'
    path = user_path
