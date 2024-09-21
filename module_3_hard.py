data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban',True, ('Urban2', 35))}])]
list_total = []


def unpack(data_structure):
    global calculate
    list_structure = list(data_structure)
    for k in range(len(list_structure)):
        if type(list_structure[k]) == int or type(list_structure[k]) == float:
            list_total.append(list_structure[k])
        elif type(list_structure[k]) == str:
            list_total.append(len(list_structure[k]))
        elif type(list_structure[k]) == tuple or type(list_structure[k]) == list or type(list_structure[k]) == set:
            curr_element = list_structure[k]
            unpack(curr_element)
        elif type(list_structure[k]) == bool:
            list_total.append(int(list_structure[k]))
        elif type(list_structure[k]) == dict:
            dict_keys = list(list_structure[k].keys())
            dict_value = list(list_structure[k].values())
            unpack(dict_keys)
            unpack(dict_value)
    calculate = sum(list_total)
    return calculate


unpack(data_structure)
print('cуммируемый список: ', list_total)
print('сумма: ', calculate)
