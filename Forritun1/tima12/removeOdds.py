def extract_evens(int_list):
    e = []
    for i in int_list:
        if i % 2 == 0:
            e.append(i)

    return e


def remove_odds(int_list):
    for i in range(len(int_list)-1,-1,-1):
        if int_list[i] % 2 != 0:
            int_list.pop(i)

