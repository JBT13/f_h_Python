n = int(input())

command = {}

for _ in range(n):
    name = input()
    value, key = name.split()
    if value == "+":
        command[key] = name

    elif value == "?":
        if key in command:
            print("Jebb")
        else:
            print("Neibb") 

    elif value == "-":
        if key in command:
            del command[key]