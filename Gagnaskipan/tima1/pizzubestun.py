n = int(input())

price_ls = []
for _ in range(n):
    pizza = input()
    pizza1, price = pizza.split(" ")
    price_ls.append(int(price))

if len(price_ls) == 1:
    print(price_ls[0])

sum = 0
price_ls.sort(reverse=True)

if len(price_ls) % 2 == 0:
    for i in range(0, len(price_ls), 2):
        if i + 1 < len(price_ls):
            num1 = price_ls[i]
            num2 = price_ls[i+1]

            max_num = max(num1, num2)

            sum += max_num

if len(price_ls) % 2 != 0:
    for i in range(0, len(price_ls)-1, 2 ):
        if i + 1 < len(price_ls):
            num1 = price_ls[i]
            num2 = price_ls[i+1]

            max_num = max(num1, num2)

            sum += max_num
    
    sum += price_ls[-1]


print(sum)
