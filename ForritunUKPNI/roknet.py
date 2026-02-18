def inntak(i, word):
    if word == "SATT":
        dic[i] = True

    if word == "OSATT":
        dic[i] = False

def ekki(i, n):
    a = dic[i]
    dic[n] = not a

def og(num1,num2,num3):
    a = dic[num1]
    b = dic[num2]
    dic[num3] = a and b

def eda(num1,num2,num3):
    a = dic[num1]
    b = dic[num2]
    dic[num3] = a or b

def utakk(num):
    if dic[num] == True:
        print(f"{num} SATT")

    if dic[num] == False:
        print(f"{num} OSATT")

n = int(input())

dic = {}

for _ in range(n):
    a = input()
    if "INNTAK" in a:
        func,num,boole = a.split(" ")
        inntak(num, boole)

    if "EKKI" in a:
        func,num,boole = a.split(" ")
        ekki(num,boole)

    if "OG" in a:
        func,num1,num2,num3 = a.split(" ")
        og(num1,num2,num3)

    if "EDA" in a:
        func,num1,num2,num3 = a.split(" ")
        eda(num1,num2,num3)

    if "UTTAK" in a:
        func,num = a.split(" ")
        utakk(num)