n = int(input())
m = int(input())

lid = input()
team = lid.split(" ")

list = [0] * n

for i in range(m):
    stig = input().split(" ")
    
    for j in range(len(stig)):
        list[j] += int(stig[j])

max = list[0]
winner = 0

for i in range(1, n):
    if list[i] > max:
        max = list[i]
        winner = i

print(team[winner])
