from DataStructures.List  import array_list as al

def new_list():
    newlist = {
        'elements':[],
        'size': 0,
    }
    return newlist

def get_element(my_list, index):
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):

    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first (my_list,e):
    my_list = al.new_list()
    my_list = al.add_first(my_list,1)

    return my_list


def add_last (my_list,e):
    my_list = al.new_list()
    my_list = al.add_last(my_list,1)

    return my_list

def size (my_list):
    my_list = al.new_list()
    print(al.size(my_list))

def first_element (my_list):
    my_list = al.new_list()
    print(al.first_element(my_list))

def is_empty(my_list):
    size = my_list['size']
    if size > 0:
        empty = False
    else:
        empty = True
    return empty

def size(my_list):
    size = my_list['size']
    return size

def last_element(my_list):
    return last_element

def delete_element(my_list,p):
    del my_list['elements'][p]
    return my_list

def remove_first(my_list):
    first_element = my_list['elements'][0]
    del my_list['elements'][0]
    my_list['size'] -= 1
    return first_element

def remove_last(my_list):
    last_element = my_list['elements'][my_list['size']-1]
    del my_list['elements'][my_list['size']-1]
    my_list['size'] -= 1
    return last_element

def insert_element(my_list, e, pos):
    my_list['element'].insert(pos,e)
    my_list['size'] += 1
    return my_list

def exchange(my_list, p1, p2):
    pos_1 = my_list['elements'][p1]
    pos_2 = my_list['elements'][p2]
    my_list['elements'][p1] = pos_2
    my_list['elements'][p2] = pos_1
    return my_list

def change_info (my_list,p, n_info):
    my_list['elements'][p] = n_info
    return my_list

def sub_list(my_list, pos_i, n_e):
    list_sub = new_list()
    for i in range (pos_i, my_list['size']):
        list_sub['elements'].insert(-1,my_list['elements'][i])
        list_sub['size'] += 1
    return list_sub