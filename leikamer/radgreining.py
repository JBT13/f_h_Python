n, m = map(int, input().split())

ls = "?"*n  

# def check(ls, num, text):
#     if ls[num-1:len(text)] == ls[num-1:] 


for _ in range(m):
    num, text = input().split()
    num = int(num)

    if ls[num-1] == "?":
        ls[num-1:len(text)] = text

    # else:
    #     check(ls,num,text)


print(ls)



