import sys

my_dict = {}
lines = sys.stdin.readlines()

try:
    separator_index = lines.index('\n')
except ValueError:
    separator_index = len(lines)


for line in lines[:separator_index]:
    word1, word2 = line.strip().split()
    my_dict[word2] = word1

for line in lines[separator_index + 1:]:
    word = line.strip()
    if word in my_dict:
        print(my_dict[word])
    else:
        print("eh")  

