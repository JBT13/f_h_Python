num = int(input())
numbers = []

while num > 0:
    numbers.append(num)
    num = int(input())

print(max(numbers))