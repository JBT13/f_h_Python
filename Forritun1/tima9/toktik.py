n = int(input())
scores = {}

for _ in range(n):
    entry = input()
    name, points = entry.split()
    points = int(points)

    if name in scores:
        scores[name] += points
    else:
        scores[name] = points

max_name = max(scores, key=scores.get)
print(max_name)