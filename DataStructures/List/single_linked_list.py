from . import list_node as node

def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
            }
    return newlist  

def get_element(my_list,pos):
    if pos < 0 or pos >= my_list["size"]:
        return None
    nodo_actual = my_list["first"]
    
    for i in range(pos):
        nodo_actual = nodo_actual["next"]
        
    return nodo_actual["info"]

def is_present(my_list, element, cmp_function):
    is_in_array=False
    temp=my_list["first"]
    count=0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"])==0:
            is_in_array=True
        else:
            temp=temp["next"]
            count+=1
            
    if not is_in_array:
        count= -1
    return count

def add_first(my_list, element):
    nuevo_nodo = node.new_single_node(element)
    nuevo_nodo["next"] = my_list["first"]  
    my_list["first"] = nuevo_nodo
    
    if my_list["size"] == 0:
        my_list["last"] = nuevo_nodo
        
    my_list["size"] += 1
        
    return my_list

def add_last(my_list, element):
    nuevo_nodo = node.new_single_node(element)
    
    if my_list["size"] == 0:
        my_list["first"] = nuevo_nodo
        my_list["last"] = nuevo_nodo
    else:
        my_list["last"]["next"] = nuevo_nodo
        my_list["last"] = nuevo_nodo
        
    my_list["size"] += 1
    return my_list

def is_empty(my_list):
    tamaño = size(my_list)
    if tamaño == 0:
        return True
    else: 
        return False

    
def size(my_list):
    return my_list["size"]

def first_element(my_list):
    tamaño = size(my_list)
    if tamaño > 0:
        return my_list["first"]["info"]
    
def last_element(my_list):
    tamaño = size(my_list)
    if tamaño > 0:
        return my_list["last"]["info"]
    
def remove_first(my_list):
    if is_empty(my_list):  
        return None
    
    nodo_removido = my_list["first"]
    my_list["first"] = nodo_removido["next"]
    my_list["size"] -= 1
    
    if my_list["size"] == 0:
        my_list["last"] = None
        
    return nodo_removido["info"]

def remove_last(my_list):
    if is_empty(my_list):
        return None
    
    if my_list["size"] == 1:
        elemento = my_list["first"]["info"]
        my_list["first"] = None
        my_list["last"] = None
        my_list["size"] = 0
        
        return elemento
    
    nodo_actual = my_list["first"]
    
    while nodo_actual["next"] != my_list["last"]:
        nodo_actual = nodo_actual["next"]
    
    elemento = my_list["last"]["info"]
    nodo_actual["next"] = None
    my_list["last"] = nodo_actual
    my_list["size"] -= 1
        
    return elemento

def insert_element(my_list, element, pos):
    nodo = node.new_single_node(element)
    tamaño = size(my_list)
    if pos < 0 or pos > tamaño:
        return None
    
    if pos == 0:
        return add_first(my_list, element)
        
    if pos == tamaño:
       return add_last(my_list, element)
   
    nodo_anterior = my_list["first"]
    
    for i in range(pos - 1):
        nodo_anterior = nodo_anterior["next"]
        
    nodo["next"] = nodo_anterior["next"]
    nodo_anterior["next"] = nodo
    my_list["size"] += 1
        
    return my_list

def delete_element(my_list, pos):
    tamaño = size(my_list)
    if pos < 0 or pos >= tamaño:
        return my_list

    if pos == 0:
        remove_first(my_list)
        return my_list

    nodo_anterior = my_list["first"]

    for i in range(pos - 1):
        nodo_anterior = nodo_anterior["next"]

    nodo_removido = nodo_anterior["next"]
    nodo_anterior["next"] = nodo_removido["next"]

    if pos == tamaño - 1:
        my_list["last"] = nodo_anterior

    tamaño -= 1

    return my_list


def change_info(my_list, pos, new_info):
    tamaño = size(my_list)
    if pos < 0 or pos >= tamaño:
        return my_list

    nodo_actual = my_list["first"]

    for i in range(pos):
        nodo_actual = nodo_actual["next"]

    nodo_actual["info"] = new_info

    return my_list

def exchange(my_list, pos1, pos2):
    tamaño = size(my_list)
    if pos1 < 0 or pos1 >= tamaño:
        return my_list

    if pos2 < 0 or pos2 >= tamaño:
        return my_list

    nodo1 = my_list["first"]
    nodo2 = my_list["first"]

    for i in range(pos1):
        nodo1 = nodo1["next"]

    for i in range(pos2):
        nodo2 = nodo2["next"]

    nodo1["info"], nodo2["info"] = nodo2["info"], nodo1["info"]

    return my_list
  

    
    
        
    
