n = int(input())

cpu = []
memory = []
web = []


for _ in range(n):
    a,b,c = input().split()
    if a == "J":
        cpu.append(1)

    if b == "J":
        memory.append(1) 

    if c == "J":
        web.append(1)

total = 0
for item in range(n):
    try:
        total += memory.pop()
        total += cpu.pop()
        total += web.pop()

    except:
        break

print(total//3)
   
    