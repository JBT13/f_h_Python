string_input = ""
list = []
while string_input != "q".lower():
    string_input = input()
    if string_input == "q":
        list.append(string_input)

print(list)
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