a = map(str, input())

vowels = ["a","e","i","o","u","y","A","E","I","O","U","Y"]
list = []
for i in a:
    if i in vowels:
        list.append(i)

print("".join(list))