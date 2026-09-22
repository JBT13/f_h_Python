n = int(input())
m = int(input())

answer1 = abs(n - m)
answer2 = abs(360-n + m) 
answer3 = abs(360-m + n) 

if answer1 < answer2 and answer1 <= answer3:
    print(answer1)

elif answer3 < answer2 and answer3 <= answer1:
    print(answer3)

else:
    print(answer2)

