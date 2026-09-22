n = int(input())

letters = "abcdefghijklmnopqrstuvwxyz"

dic = {}
for _ in range(n):
    english, icelan = input().split()
    dic[english] = icelan
    
    
m = int(input())

for _ in range(m):
    name = input()
        
    if name in dic.keys():
        print(dic[name])

    elif not name.isalpha():
        print(name)

    elif name :
        print(f"?{name}?")
    
        
    