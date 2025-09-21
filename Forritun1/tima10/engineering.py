import sys

sentence = " ".join(line.strip() for line in sys.stdin if line.strip())
words = sentence.split()
word_count = {}
result = []
seen = {}

for word in words:
    lower_word = word.lower()
    word_count[lower_word] = word_count.get(lower_word, 0) + 1


for word in words:
    lower_word = word.lower()
    if word_count[lower_word] > 1:
        if lower_word in seen:
            result.append(".")
        else:
            result.append(word)
            seen[lower_word] = True
    else:
        result.append(word)

print(" ".join(result))