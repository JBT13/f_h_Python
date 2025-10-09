a, b = input().split(":")
c, d = input().split(":")

hour1 , minute1 = int(a), int(b)
hour2 , minute2 = int(c), int(d)

time1 = (hour1 * 60) + minute1
time2 = (hour2 * 60) + minute2

if time1 > time2:
     difer = (time2 + 1440) - time1

else:
     difer = time2 - time1

print(difer)