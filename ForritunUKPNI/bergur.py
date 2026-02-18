a = int(input())

ma_ls = list(map(int, input().split()))

rang = 0
count = 0
geym = 0
for i in range(len(ma_ls)-1, -1,-1):
    if ma_ls[i] > ma_ls[i-1]:
        count += ma_ls[i]
        rang += 1

    elif ma_ls[i] < ma_ls[i-1]:
        geym = i
        break

for i in range(len(ma_ls)-rang):
    count += ma_ls[geym]

print(count)