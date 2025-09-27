s = input()

result = []

for i in range(len(s)):
    if s[i] == "<":
        if result:
            result.pop()
    else:
        result.append(s[i])

print("".join(result))