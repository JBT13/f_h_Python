n = int(input())

for _ in range(n):
    dic = {}
    text = input().split(" ")
    for word in text:
        if word[0] not in dic:
            dic[word[0]] = 1
        else:
            dic[word[0]] += 1

    m = ""
    c = 0
    for k, v in dic.items():
        if v > c:
            c = v
            m = k

    print(m)
        
    
    
    

