import sys

vowels = "aeiouAEIOU"

for line in sys.stdin:
    words = line.strip().split()
    result = []

    for word in words:
        if word[0] in vowels:
            result.append(word + "yay")
        else:
            index = 0
            while index < len(word) and word[index] not in vowels:
                index += 1
            if index == len(word):
                result.append(word + "ay")
            else:
                result.append(word[index:] + word[:index] + "ay")

    print(" ".join(result))