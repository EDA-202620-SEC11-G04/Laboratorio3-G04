import single_linked_list as sn
from DataStructures.List import list_node as ln


def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }


    return newlist


def get_element(my_list,pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos +=1
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    return node["info"]


def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
    
    if not is_in_array:
        count = -1
    return count


def add_first(my_list,e):
    n = ln.new_single_node(e)
    n["next"] = my_list["first"]
    my_list["first"] = n
    my_list["size"] +=1
    return my_list
    
    
def add_last(my_list,e):
    n = ln.new_single_node(e)
    searchpos = 0
    previo = my_list["first"]
    while searchpos != my_list["size"]:
        if searchpos == my_list["size"]-1:
            previo["next"] = n
            n["next"] = None
            my_list["last"] = n
        searchpos += 1
        previo = previo["next"]
    my_list["size"] +=1
    return my_list
    
    
def size(my_list):
    respuesta = my_list["size"] 
    return respuesta


def first_element(my_list):
    respuesta = my_list["first"]
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    return respuesta


def is_empty(my_list):
    if my_list["size"] == 0:
        respuesta = True
    if my_list["size"] != 0:
        respuesta = False
    return respuesta


def last_element(my_list):
    respuesta = my_list["last"]
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    return respuesta


def delete_element(my_list,pos):
    searchpos = 0
    node = my_list["first"]
    previo = None 
    while searchpos <= pos:
        if searchpos == pos:
             node = node["next"]
             previo["next"] = node   
             break 
        previo = node 
        node = node["next"]
        searchpos += 1
    my_list["size"] -= 1
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list


def remove_first(my_list):
    my_list["first"] = my_list["first"]["next"]
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list


def remove_last(my_list):
    searchpos = 0
    node = my_list["first"]
    previo = None
    while searchpos < my_list["size"]-1:
        if node["next"] == None:
            previo["next"] = None
            my_list["last"] = previo
        previo = node 
        node = node["next"]
        searchpos += 1
    my_list["size"] -= 1
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list
    

def insert_element(my_list,e,pos):
    searchpos = 0
    n = ln.new_single_node(e)
    node = my_list["first"]
    previo = None
    while searchpos <= pos:
        if searchpos == pos:
            node = node["next"]
            previo["next"] = n
            n["next"] = node
        previo = node
        searchpos += 1
    my_list["size"] += 1 
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list 


def change_info(my_list,pos,new_info):
    searchpos = 0
    node = my_list["first"]
    while searchpos <= pos:
        if searchpos == pos:
            node["info"] = new_info
        node = node["next"]
        searchpos += 1
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list


def exchange(my_list,pos_1,pos_2):
    temp1 = None
    temp2 = None
    temp1_1 = None
    temp2_1 = None
    node = my_list["first"] 
    searchpos = 0
    while searchpos != my_list["size"]:
        if searchpos == pos_1:
            temp1_1 = node
            temp1 = node["info"]
        if searchpos == pos_2:
            temp2_1 = node
            temp2 = node["info"]
        node = node["next"]
        searchpos += 1
    temp2_1["info"] = temp1
    temp1_1["info"] = temp2
    if pos_1 < 0 or pos_1 > size(my_list):
        raise Exception('IndexError: list index out of range')
    if pos_2 < 0 or pos_2 > size(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list


def sub_list(my_list,pos,num_elements):
    nueva_lista = []
    searchpos = 0
    node = my_list["first"]
    contador = 0
    while searchpos != my_list["size"]:
        if searchpos == pos:
            while contador != num_elements and searchpos != my_list["size"]:
                nueva_lista.append(node["info"])
                node = node["next"]
                contador += 1
        searchpos += 1
        node = node["next"]
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    return nueva_lista
        