def list_to_int_tuple(search_list):
    new_list = []
    for i in search_list:
        try:
            i = int(i)
            new_list.append(i)
        except:
            continue
    
    return tuple(new_list)
