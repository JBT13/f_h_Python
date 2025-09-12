floated = input()

list_str = floated.split()
#Convert each string in the list to an integer
# This creates a new list with the numbers as integers
list = [float(x) for x in list_str]

if len(list) < 3:
    print("At least 3 scores needed!")

else:
    sorted(list)
    list.remove(min(list))
    list.remove(min(list))
    list.remove(min(list))
    print(f"Sum of scores (3 lowest removed): {sum(list)}")
