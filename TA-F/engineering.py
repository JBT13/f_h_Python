
import sys

ls = []
ls2 = []

for line in sys.stdin:
    line = line.strip()
    for word in line.split():
        if word.lower() not in ls and word.lower() not in ls2:
            ls.append(word.lower())
            ls2.append(word)

        else:
            ls.append(".")
            ls2.append(".")

print(" ".join(ls2))


