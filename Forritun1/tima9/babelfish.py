# import sys

# translator = {}

# while True:
#     a = input()
#     if a == "":
#         break
#     name, foreign = a.split()
#     translator[foreign] = name

# words = []
# for line in sys.stdin:
#     word = input()
#     words.append(word)

# for word in words:
#     if word in translator:
#         print(*{translator[word]})
#     else:
#         print("eeehh")

import sys

translator = {}

# Reads all lines from standard input and builds the translator dictionary
lines = sys.stdin.readlines()

# Find the empty line that separates the two sections of input
try:
    separator_index = lines.index('\n')
except ValueError:
    # If there is no blank line, all lines are dictionary entries
    separator_index = len(lines)

# Populate the translator dictionary
for line in lines[:separator_index]:
    # Use .strip() to remove the newline character at the end of each line
    name, foreign = line.strip().split()
    translator[foreign] = name

# Process the words to translate
for line in lines[separator_index + 1:]:
    word = line.strip()
    if word in translator:
        print(translator[word])
    else:
        print("eh") 

