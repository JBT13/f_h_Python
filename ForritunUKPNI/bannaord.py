ban = input()
sentence = input().split(" ")
ban = set(ban)
list = []

for word in sentence:
    flagged = False
    for ch in word:
        if ch in ban:
            flagged = True

    if flagged:
        list.append("*" * len(word))
    else:
        list.append(word)

print(*list)