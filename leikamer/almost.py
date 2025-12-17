# n = int(input())

# numbers = list(map(int,(input().split())))

# a_list = []
# for index, number  in enumerate(numbers):
#     for index2, number2 in enumerate(numbers):
#         if number2 % number == 0 and index != index2:
#             a_list.append(str(index+1))    
#             a_list.append(str(index2+1)) 
#             break

#     if number2 % number == 0 and index != index2:
#         break

# for i, j in a_list:
#     print(f"{i} {j}")      

# print(" ".join(a_list[0:2]))

# def double_evens(nums):
#     new_nums = []
#     i=0
#     while i < len(nums):
#         if nums[i]%2==0:
#             new_nums.insert(i,nums[i])
#         i+=1

#     return new_nums

# print(double_evens([2,4]))

# def mystery(x):
#     if type(x)==int:
#         return x*2
#     elif type(x) ==float:
#         return x/2
#     else:
#         print("error")

# print(mystery("4"))

# def merge_sorted(list1, list2):
#     new_list = []
#     for i in list1:
#         for j in list2:
#             if i != j and i not in new_list and j not in new_list:
#                 new_list.append(i)
#                 new_list.append(j) 
    
#     return new_list

# print(merge_sorted([1,3,7],[2,1,4,9]))

# def add_to(bucket=[], x=0):
#     bucket.append(x)
#     return bucket

# def make_counter(start=0):
#     n = [start]
#     def  inc():
#         n[0] += 1
#         return n[0]
#     return inc


# print(add_to(x=1))
# print(add_to(x=2))
# c = make_counter(5)
# print(c(), c(), c())
# print(add_to(x=3))

# i = 0
# while i < 5:

#     print(i)
#     i += 1

# keys = ["a", "b", "c"]
# values = [1,2,3]

# my_dict = dict((keys, values))
# print(my_dict)
import math
print(len("mississippi"))

a = math.factorial(11)
b = math.factorial(2)*math.factorial(4)*math.factorial(4)

print(a/ b)