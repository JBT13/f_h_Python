text = input()

parts = [] 
counts = []

for i in range(len(text)):
    for j in range(i + 1, len(text) + 1):
        part = text[i:j]

        if part not in parts:
            parts.append(part)

            count = 0

            for k in range(len(text) - len(part) + 1):
                if text[k:k + len(part)] == part:
                    count = count + 1

            counts.append(count)


for count in range(max(counts), 0, -1):
    same = []

    for i in range(len(parts)):
        if counts[i] == count:
            same.append(parts[i])

    same.sort()

    for part in same:
        print(count, part)