from typing import List, Tuple


def list_to_bool_tuple(a_list: List[str]) -> Tuple[bool]:
    """Returns a tuple with each element in the list converted to bool.

    First converts any integers to int.
    """
    tuple_list = []
    for i in a_list:
        try:
            i = int(i)
            tuple_list.append(bool(i))
        except:
            tuple_list.append(bool(i))


    return tuple(tuple_list)
