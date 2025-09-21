n = int(input())

city_count = {}

for _ in range(n):
    name = input()
    city = input()
    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1

for city, count in city_count.items():
    print(city, count)

