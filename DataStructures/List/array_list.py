def new_list():
    newlist = {
        'elements': [],
        'size': 0,
            }
    return newlist

<<<<<<< HEAD
def add_first(my_list, element):
    my_list['elements'].insert(0, element)
    my_list['size'] += 1
    return my_list
=======
def get_element(my_list, index):
    
    return my_list['elements'][index]

def is_present(my_list, element, cmp_function):
    
    size = my_list['size']
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list['elements'][keypos]
            if cmp_function(info, element) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1
>>>>>>> 17c9aa3fab6e53abd35c9e68a3f26f6054e0f207
