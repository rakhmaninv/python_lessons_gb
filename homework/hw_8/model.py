import csv
import json


def get_data():
    with open('homework\hw_8\data\data.csv', 'r', encoding='utf-8-sig') as f:
        data = list(csv.DictReader(f))
    return data

def save_data_csv(data, key, name= 'data'):
    with open(f'homework\hw_8\data\{name}.csv', 'w', newline='', encoding='utf-8-sig') as f:
        csv.writer(f).writerow(key)
        csv.DictWriter(f, key).writerows(data)

def export_to_json(data, name):
    with open(f'homework\hw_8\data\{name}.json', 'w', encoding='utf-8-sig') as f:
        json.dump(data, f)

def employee_search(data, param):
    return [i for i in data if all(i[key] == value for key, value in param.items())]

def job_title_selection(data, job):
    return list(filter(lambda x: x['job_title'] == job, data))

def salary_selection(data, salary_range):
    return list(filter(lambda x: float(x['salary']) >= min(salary_range) 
                                and float(x['salary']) <= max(salary_range), data))

def add_employee(data, keys, employee_info):
    id = [str(max([int(i['id']) for i in data]) + 1)]
    data.append(dict(zip(keys, id + employee_info.split())))

def delete_employee(data, id):
    return list(filter(lambda x: x['id'] != id, data))

def update_eployee(data, id, employee_info):
    employee = next(i for i in data if i['id'] == id)
    employee.update(employee_info)

