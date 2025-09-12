# days = int(input())
# list = []

# while days != len(list):
#     temp = int(input())
#     list.append(temp)

# print(max(list), min(list))

days = int(input())

temp_input = input()

temp_list_str = temp_input.split()

#Convert each string in the list to an integer
# This creates a new list with the numbers as integers
temp_list = [int(x) for x in temp_list_str]

print(max(temp_list), min(temp_list))
