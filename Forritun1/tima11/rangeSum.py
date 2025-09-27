def sum_of_range(start, end, step):
    sigma = (end - start) // step
    list = []
    for i in range(sigma+1):
        value = start + i * step
        list.append(value)
    
    return sum(list)

