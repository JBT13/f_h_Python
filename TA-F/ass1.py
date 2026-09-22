n = ""

while n != "q" and n != "Q":
    n = input()

    if n.isnumeric():
        n = int(n)

        count = 0
        for i in range(1,n+1):
            if n % i == 0:
                count += 1
        
        if count >= 10:
            print("yes")
            
        else:
            print("no")

    else:
        continue

m = int(input())

for i in range(10,m+1):
    digitsum = [int(d) for d in str(i)]
    if sum(digitsum)**2 == i or sum(digitsum)**3 == i:
        print(i)





        