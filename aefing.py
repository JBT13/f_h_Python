# # def count_vowels(text):
# #     vowels = ["a","e","i","o","u"]
# #     count = 0
# #     for ch in text:
# #         if ch in vowels:
# #             count += 1
        
# #     return count

# # a = count_vowels("Butterflies")
# # print(a)

# list = ["q","w","t","y","u","p","f","g","h","j","k","z","x"]

# letter1 = "a"
# letter2 = "o"
# letter3 = "e"

# for i in list:
#     for j in list:
#         word = letter1 + i + letter2 + j + letter3
#         print(word)
    
# def n():
#     global x
#     x = 5

# x = 10
# n()
# print(x)
# sum = 0
# for i in range(5):
#     print("a")
#     for j in range(3):
#         print("b")
    
# a = [1,2,3]
# b = [4,5,6]

# a.append(b)
# c = a[:]

# b[0] = 5
# print(c)

# a = {1,3,5,7,9}
# b = {2,3,5,7}

# print(a.remove(2))

# def m():
#     global x 
#     x = 5

# x = 10
# m()
# print(x)

# numbers = input().split("+")

# for i in numbers

# try:
#     num_a = int(a, 0)
#     num_b = int(b, 0)
    
#     if a.startswith('0x') or b.startswith('0x'):
#         print(hex(num_a + num_b))
#     else:
#         print(num_a + num_b)

# except ValueError:
#     print(a + b)

# n = int(input())
# big = []
# for _ in range(n):
#     x = int(input())
#     big.append(x)
    
# if n > max(big):
#     print(n)

# else:
#     print(max(big))

# n = int(input())

# if n % 4 == 0:
#     print(n)

# elif n % 4 == 1:
#     print(1)

# elif n % 4 == 2:
#     print("Gunnar")

# elif n % 4 == 3:
#     print("Enginn")


# a = input()

# r = ""

# for i in range(len(a)-1,-1,-1):
#     r += a[i]
    
# if r == a:
#     print("Palindrome")

# else:
#     print("Nothing special about this string :(")
    
# a = int(input())

# b = input().split()

# ls = []
# for i in b:
#     ls.append(int(i))

# op = max(ls)
# lo = min(ls)
# print(op, lo)

# def sume(n):
#     if n == 0:
#         return 1
    
#     p = 1
#     num = n
#     while n > p:
#         num += (n-p)
#         p += 1 

#     return num

# a = int(input())

# ls = []
# for i in range(a):
#     a,b = map(int, input().split())
#     ls.append(b)

# for i in range(0,len(ls)):
#     print(f"{i+1} {sume(ls[i])+ls[i]}")

# n = int(input())
# my_d = {}

# for i in range(1,n+1):
#     my_d[i] = 0 


# for i in range((n//2)+1):
#     a,b = map(int, input().split()) 
#     my_d[a] += 1    
#     my_d[b] += 1

# ls = []

# for index, value in my_d.items():
#     if value == 2:
#         ls.append(index)

# x = 0
# y = 0
        
# if ls[0] > ls[-1]:
#     x = ls[-1]   
#     y = ls[0]

# else:
#     x = ls[0]
#     y = ls[-1]

# print(x, y)


# def hello(n):
#     print(n+1)

# print(hello(2))

# n = int(input())

# a = input()

# count = 0
# count1 = 0
# count2 = 0

# for i in a:
#     if i == "G":
#         count += 1

#     if i == "A":
#         count1 += 1

#     if i == "D":
#         count2 += 1

# print((count/(n-count2))*100)


# n = int(input())

# k = 0
# i = 0
# while (2<<i) <= n:
#         k += 1
#         i += 1

# print(k)

# n = 5
# for i in range(n):
#     for j in range(i):
#         print(i,j)

# def binco(n):
    
#     return binco(n-1)

# a = [10,20,40,30]
# ls = []
# count = 0 
# for i in range(len(a)):
#     ls.append(a[i]+count)
#     count += a[i]

# print(ls)

# ls = [[1,2]] * 3
# ls[0][1] = 3
# print(ls)

# from collections import deque

# d = deque([20,50,40], maxlen=4)
# print(d)
# d.append(10)
# print(d)
# d.appendleft(30)
# print(d)
# d.pop()
# print(d)
# d.popleft()
# print(d)

# def twoSum(nums: List[int], target: int) -> List[int]:
#     ls = []
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if nums[i] + nums[j] == target:
#                 ls.append(i)
#                 ls.append(j)
#                 return ls

l = 4
if l % 2:
    print("hello")

    

