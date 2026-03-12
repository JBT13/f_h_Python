def length_of_string(st: str): 
    if st == "":
        return 0
    
    return 1 + length_of_string(st[1:])

def linear_search(ls: list,value: object):
    if ls == []:
        return False
    
    if ls[-1] == value:
        return True 

    return linear_search(ls[0:-1], value) 

def count_instances(ls: list, value: object):
    if ls == []:
        return 0

    number = count_instances(ls[1:],value)
    if ls[0] == value:
        number += 1

    return number

def duplicates_in_list(ls:list):
    if ls == [] and len(ls) == 1:
        return False
    
    if ls[0] in ls[1:]:
        return True
    
    return duplicates_in_list(ls[1:])

def remove_duplicates(ls:list):
    if ls == []:
        return ls
    
    hello = remove_duplicates(ls[0:-1])

    if ls[0] not in ls[1:]:
        hello.append(ls[-1])

    return hello


def binary_search(ls:list, value,left, right):
    mid = (left + right) // 2 

    if left > right:
        return -1

    if ls[mid] == value:
        return mid
    
    if value < ls[mid]:
        return binary_search(ls,value,left, mid-1)

    if value > ls[mid]:
        return binary_search(ls,value,mid+1,right)


def prefix_check(sub_string,a_str):
    if len(sub_string) == 0:
        return True
    
    if len(a_str) == 0 or sub_string[0] != a_str:
        return False
    
    return prefix_check(sub_string[1:], a_str[1:])

def substring_check(substring, a_str):
    
    if len(a_str) < len(substring):
        return False
    
    if prefix_check(substring, a_str):
        return True

    return substring_check(substring, a_str[1:])

def elfish(st:str):
    if st[0] == "e":
        return elfish(st[1:])
    
    if st[0] == "l":
        return elfish(st[1:])

    if st[0] == "f":
        return True
    
    return False

def palindrome(st: str):
    if len(st) <= 1:
        return True
    
    if st[0] == st[-1]:
        return palindrome(st[1:-1])
    
    return False

d = int(input())

s1 = int(input())
s2 = int(input())
height = int(input())

r = d/2 
radius = r*r
mahjong = 3.14*radius

trapizza = (1/2)*(s1+s2)*height

if int(mahjong) > trapizza:
    print("Mahjong!")

elif trapizza > int(mahjong):
    print("Trapizza!")

else:
    print("Jafn storar!")