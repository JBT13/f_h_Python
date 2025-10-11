def hello():
    string_input = ""
    list = []
    while string_input != "q" and string_input != "Q":
        string_input = input()
        if string_input != "q" and string_input != "Q":
            list.append(string_input)
    return list

hellon = hello()
print(hellon)
# n = int(input())
# # for i in range(1,n+1):
# #     star = []
# #     for j in range(1,i+1):
# #         star.append("*"*j)

# # for i in star:
# #     print(i)

# for i in range(1,n+1):
#     stars = []
#     for _ in range(i):
#         stars.append("*")
#     print("".join(stars))

n = int(input())
list = []
for i in range(1,n+1):
    if n % i == 0:
        list.append(i)
    else:
        continue
print(*list) 

name = "viktor"
print(name[::-1])
