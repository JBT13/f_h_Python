n = int(input())
m = input().split()

ls = []

for item in m:
    if item == "🧦":
        ls.append(item)

    elif item == "👟":
        ls.pop()

if len(ls) == 0:
    print("gilt")

else:
    print("ógilt")