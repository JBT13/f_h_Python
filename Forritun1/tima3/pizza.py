y = int(input())

if y <= 2020 and y >= 1993:
    print(1000)

elif y > 2020:
    increment = (y - 2020) * 100
    print(1000 + increment)
     