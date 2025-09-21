n, k = map(int, input().split())

values = list(map(int, input().split()))

if k in values:
    position = values.index(k) + 1

if k == values[0]:
    print("fyrst")

elif k == values[1]:
    print("naestfyrst")

else:
    print(f"{position} fyrst")