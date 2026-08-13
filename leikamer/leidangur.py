def precious(listi: list, type):
    if listi == []:
        return 

    for word in listi:
        if word != type:
            listi.pop()
    
    listi.pop()

def display(listi, type):
    count = 0
    for items in listi:
        if items == type:
            count += 1

    return count

s = input()

stack = []

for letter in s:
    if letter == "p":
        stack.append("money")

    elif letter == "g":
        stack.append("gold")

    elif letter == "o":
        stack.append("jewel")

    elif letter == "P":
        precious(stack, "money")

    elif letter == "G":
        precious(stack, "gold")

    elif letter == "O":
        precious(stack, "jewel")    

    else:
        continue

if len(stack) == 0:
    print("Neibb")

else:
    print(display(stack,"money"))
    print(display(stack,"gold"))
    print(display(stack,"jewel"))

