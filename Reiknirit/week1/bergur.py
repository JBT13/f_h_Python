n = int(input())
m = input().split()

int_list = [int(x) for x in m]

sum = 0
num = int_list[-1]

for i in range(len(int_list)-1,0,-1):
    a = int_list[i-1]

    if a <= num:
        sum += num
        num = a

    else:
        sum += num

sum += num

print(sum)



