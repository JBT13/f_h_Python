columns = int(input())
rows = int(input())

count = 0

for _ in range(rows):
    cars = input()
    count += cars.count(".")

length = rows * columns
ratio = count/ length

print(ratio)