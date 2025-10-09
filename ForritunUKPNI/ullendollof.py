n = int(input())

list1 = input().split()

value = 13

wrap = value % n - 1

result = list1[wrap]

print(result)