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


a = [1,2,3]

print(a)
print(*a)
