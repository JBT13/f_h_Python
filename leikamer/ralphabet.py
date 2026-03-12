s = input()

m = ""
ls = []

for i in s:
    if i in "aeiouAEIOU":
        ls.append(i)

for i in s:
    if i in "aeiouAEIOU":
        m += ls[-1]
        ls.pop()

    else:
        m += i

print(m)        
    

