ammount = int(input())
list = []

while ammount != len(list):
    numbers = int(input())
    list.append(numbers)

for number in list[::-1]:
    print(number)



