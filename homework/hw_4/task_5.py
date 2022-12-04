# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

def get_power(arg: str):
    if 'x' not in arg:
        return 0 
    elif 'x' in arg and '^' not in arg:
        return 1
    else:
        return int(arg.split('^')[1])

def get_coefficient(arg: str):
    if 'x' not in arg:
        return int(arg)
    elif arg.split('x')[0] == '-':
        return -1
    elif  arg.split('x')[0] == '':
        return 1
    else:
        return int(arg.split('x')[0])

def sum_of_two_dictionaries(a: dict, b: dict):
    return {key: a.get(key, 0) + b.get(key, 0) for key in a | b}

def polynomial_dict_to_list(d: dict):
    pol = []
    for key, value in d.items():
        if key == 0:
            pol.append(f'{value}')
        elif key == 1:
            pol.append(f'{value}x')
        else:
            pol.append(f'{value}x^{key}')
    return pol

def term_separation(s: str):
    return list(filter(None, s.replace(' ', '').replace('-', '+-').split('+')))

with open('homework\\hw_4\\5_first.txt') as f:
    first_pol = f.read() 
    term_sep_first = term_separation(first_pol)
    pol_dict_first = {get_power(i): get_coefficient(i) for i in term_sep_first}

with open('homework\\hw_4\\5_second.txt') as s:
    second_pol = s.read()
    term_sep_second = term_separation(second_pol)
    pol_dict_second = {get_power(i): get_coefficient(i) for i in term_sep_second}

dict_sum = dict(sorted(sum_of_two_dictionaries(pol_dict_first, pol_dict_second).items(),reverse= True, key= lambda i: i[0]))

with open('homework\\hw_4\\5_sum_of_polynomials.txt', 'w') as data:
    data.write(' + '.join(polynomial_dict_to_list(dict_sum)).replace('+ -', '- ').replace(' 1x', ' x'))