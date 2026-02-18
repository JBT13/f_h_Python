from random import randint

def a_to_power_b (a:int ,b:int) -> int:
    # num = 1
    # for _ in range(b):
    #     num *= a
    # return num 
    # My answer
    
    # num = 1
    # while b > 0:
    #     if b % 2 == 1:
    #         num *= a
    
    #     a *= a
    #     b //= 2
    # return num

    return a**b # O(log(y))

def mul_pos(a:int, b:int) -> int: 
    num = 1
    if a > b:
        for _ in range(b):
            num += a
        return num 

    for _ in range(a):
        num += b
        return num

def min_number(list_n: list[int]) -> int:
    min_number = list_n[0]
    for i in range(len(list_n)):
        if min_number > list_n[i]:
            min_number = list_n[i]

    return min_number

def random_number_list(size):
    list_num = []
    for _ in range(size):
        random = randint(1,6)
        list_num.append(random)

    return list_num

def turn_to_str(list_num: list[int]):
    crazy = []
    for i in range(len(list_num)):
        num = str(i)
        crazy.append(num)

    print(",".join(crazy))

def incr_loc_index(list_num: list[int]):
    random = randint(0,len(list_num))

    for i in range(len(list_num)):
        if i == random:
            list_num[i] += 1

    return list_num

def switch_items(list_num :list[int]):
    random = randint(0,len(list_num)-1)

    for i in range(len(list_num)):
        if i == random and i != len(list_num)-1:
            number = list_num[i]
            list_num[i] = list_num[i+1]
            list_num[i+1] = number

    return list_num

def switch_items2(list_num :list[int]):
    random = randint(0, len(list_num)-1)
    random2 = randint(0,len(list_num)-1)

    number = list_num[random]
    list_num[random] = list_num[random2]
    list_num[random2] = number

    return list_num

def ordered_insertion(list_num: list[int]):
    random = randint(1,6)

    my_l = []
    for index, value in enumerate(list_num):
        if value > random:
            my_l.append((index-1,random))

        elif random > value:
            my_l.append((index+1,random))

    tup = my_l[-1]
    index, ra = tup

    list_num.insert(index,ra)

    return list_num

print(ordered_insertion([1,2,3,4]))




