import list_node as node

def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
            }
    return newlist  

def get_element(my_list,pos):
    searchpos=0
    node=my_list["first"]
    while searchpos<pos:
        node=node["next"]
        searchpos+=1
    return node["info"]

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
    node = node.new_single_node(element)
    node["next"] = my_list["first"]  
    my_list["first"] = node
    
    if my_list["size"] == 0:
        my_list["last"] = node
        my_list["size"] += 1
        
    return my_list

def add_last(my_list, element):
    node = node.new_single_node(element)
    
    if my_list["size"] == 0:
        my_list["first"] = node
        my_list["last"] = node
    else:
        my_list["last"]["next"] = node
        my_list["last"] = node
        
    my_list["size"] += 1
    return my_list

def is_empty(my_list):
    return True if my_list["size"] == 0 else False

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
    tamaño = size(my_list)
    if tamaño > 0:
        nodo_removido = my_list["first"]
        my_list["first"] = nodo_removido["next"]
        my_list["size"] -= 1
        
    return nodo_removido["info"]

def remove_last(my_list):
    tamaño = size(my_list)
    if tamaño > 0:
        nodo_removido = my_list["first"]
        my_list["first"] = nodo_removido["next"]
        my_list["size"] -= 1
        
    return nodo_removido["info"]

def insert_element(my_list, element, pos):
    nodo = node.new_single_node(element)
    tamaño = size(my_list)
    if pos not in range(tamaño):
        return "posición no valida"
    
    if pos == 0:
        return add_first(my_list, element)
        
    if pos == tamaño:
       return add_last(my_list, element)
   
    nodo_anterior = my_list["first"]
    for i in range(pos-1):
        nodo_anterior = nodo_anterior["next"]
        
    nodo["next"] = nodo_anterior["next"]
    nodo_anterior["next"] = nodo
    my_list["size"] += 1
    
    if my_list["last"] == nodo_anterior:
        my_list["last"] = nodo
        
    return my_list
  

    
    
        
    
