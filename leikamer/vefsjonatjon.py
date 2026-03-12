n = int(input())

cpu = []
memory = []
web = []


for _ in range(n):
    a,b,c = input().split()
    if a == "J":
        cpu.append(a)

    if b == "J":
        memory.append(b) 

    if c == "J":
        web.append(c)

if len(cpu) == 0 or len(memory) == 0 or len(web) == 0:
    print(0)

if len(cpu) == len(memory) and len(memory) == len(web) and len(web) == len(cpu):
    print(len(cpu))

if len(cpu) == len(memory) and len(memory) != len(web):
    print(len(web))

if len(cpu) != len(memory) and len(memory) == len(web):
    print(len(cpu))

if len(cpu) == len(web) and len(memory) != len(web):
    print(len(memory))


   
    