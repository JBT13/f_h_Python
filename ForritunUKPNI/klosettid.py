n = int(input())
a = list(map(int, input().split()))

a.sort3()
print(*a[::-1])