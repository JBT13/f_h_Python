# import sys
# print("--- SCRIPT START ---")
# print(f"My actual arguments are: {sys.argv}")
a = input()

try:
    first = a[0]
    second = a[1:-1]
    third = a[-1]

    flag = True
    for c in second:
        if c != "r":
            flag = False

    if first == "b" and len(second) > 2 and third in "aeiouy" and flag:
        print("Jebb")
        
    else:
        print("Neibb")

except IndexError:
    print("Neibb")