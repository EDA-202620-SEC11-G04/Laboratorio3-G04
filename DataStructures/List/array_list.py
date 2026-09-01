from operator import index


def new_list():
    newlist = {
        'elements': [],
        'size': 0,
            }
    return newlist

def get_element(my_list, index):
    return my_list['elements'][index]

def is_present(my_list, element, cmp_function):
    size = my_list['size']
    
    if size > 0:
        keyexist = False
        for keypos in range(size):
            info = my_list['elements'][keypos]
            
            if cmp_function(info, element) == 0:
                return keypos
    return -1

def add_first(my_list, element):
    my_list['elements'].insert(0, element)
    my_list['size'] += 1
    return my_list

def add_last(my_list, element):
    my_list['elements'].append(element)
    my_list['size'] += 1
    return my_list
    
def size(my_list):
    return my_list['size']  

def first_element(my_list):
    if my_list['size'] > 0:
        return my_list['elements'][0]
    else:
        return None
    
def get_element(my_list, index):
    tamaño = size(my_list)
    if (index < 0) or (index >= tamaño):
        return None
    return my_list['elements'][index]

def delete_element(my_list, index):
    tamaño = size(my_list)
    if (index < 0) or (index >= tamaño):
        return None
    else:
        my_list['elements'].pop(index)
        my_list['size'] -= 1
        return my_list

def insert_element(my_list, index, info):
    tamaño = size(my_list)
    if (index < 0) or (index > tamaño):
        return None
    else:
        my_list['elements'].insert(index, info)
        my_list['size'] += 1
        return my_list
    
def is_empty(my_list):
    tamaño = size(my_list)
    if tamaño == 0:
        return True
    else:
        return False
    
def remove_first(my_list):
    tamaño = size(my_list)
    if tamaño == 0:
        return None
    else:
        primer_elemento = my_list['elements'].pop(0)
        tamaño -= 1
        return primer_elemento
    
def remove_last(my_list):
    tamaño = size(my_list)
    if tamaño == 0:
        return None
    else:
        ultimo_elemento = my_list['elements'].pop()
        tamaño -= 1
        return ultimo_elemento
    
def change_info(my_list, index, new_info):
    tamaño = size(my_list)
    if (index < 0) or (index >= tamaño):
        return None
    else:
        my_list['elements'][index] = new_info
        return my_list
    
def exchange(my_list, pos1, pos2):
    tamaño = size(my_list)
    if (pos1 < 0 or pos1 >= tamaño) or (pos2 < 0 or pos2 >= tamaño):
        return None
    else:
        my_list['elements'][pos1], my_list['elements'][pos2] = my_list['elements'][pos2], my_list['elements'][pos1]
        return my_list
    
def sub_list(my_list, pos1, pos2):
    tamaño = size(my_list)
    if (pos1 < 0) or (pos2 >= tamaño) or (pos1 > pos2):
        return None
    else:
        lista_nueva = {
            'elements': my_list['elements'][pos1:pos2 + 1],
            'size': pos2 - pos1 + 1
        }
        return lista_nueva
  