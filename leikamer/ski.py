name = input()
hour, min = map(int,input().split(":"))
day = input()
weather = int(input())
snow = int(input())
holiday = int(input())

total = 1


if day == "sat" or day == "sun":
    total *= 2

if weather == 1:
    total *= 2

if snow == 1:
    total *= 3

if holiday == 1:
    total *= 3

h = total * hour 

m = total * min

h += m // 60


print(f"{h}:{m%60:02}")


    
