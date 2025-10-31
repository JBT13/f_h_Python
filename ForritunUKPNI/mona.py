n = input()
name = n.split(" ")
list = []

if len(name) == 1:
    print((n + " ") * 3)    
elif len(name) == 2:
    list.append(name[0])
    nafn = list[0] 
    print((nafn + " ") * 3)    
elif len(name) == 3:
    print(n)