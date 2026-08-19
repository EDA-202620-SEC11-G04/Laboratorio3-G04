def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
            }
    return newlist  

def add_first(my_list, element):
    my_list['elements'].insert(0, element)
    my_list['size'] += 1
    return array_list