n = int(input())
a, b = map(int, input().split())

result = 0
for i in range(a, b+1):
    result = result ^ i


if result == 0:
    print("Enginn")

elif result < n:
    print(result)

else:
    print("Gunnar")
