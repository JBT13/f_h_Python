# Feel free to make use of the following function in your implementations.
def find_min_and_max_index(a_list: list) -> tuple:
    """Finds the position of the lowest number and the highest number in the list."""

    min_index, max_index = 0, 0

    for i in range(1, len(a_list)):
        if a_list[i] < a_list[min_index]:
            min_index = i

        if a_list[i] > a_list[max_index]:
            max_index = i

    return min_index, max_index


def without_outliers(l):
    min_index, max_index = find_min_and_max_index(l)
    m = []
    for index, value in enumerate(l):
        if index != min_index and index != max_index:
            m.append(value)

    return m

def remove_min_and_max(l):
    minv = min(l)
    maxv = max(l)

    l.remove(minv)
    l.remove(maxv)
        


