# a, b = map(int, input().split())

# description = {}

# money = []

# for _ in range(a):
#     job = input()
#     name , salary = job.split()
#     description[name] = int(salary)

# for _ in range(b):
#     sentence = input()
#     words = sentence.split(sep=".")
#     for word in words:
#         if word in description:
#             money.append(description[word])

# print(sum(money))

import sys

# Read the first line containing the number of words in the dictionary (m)
# and the number of job descriptions (n).
# We use a try-except block to handle potential end-of-file situations.
try:
    m_str, n_str = input().split()
    m = int(m_str)
    n = int(n_str)
except (ValueError, EOFError):
    # This break is not strictly necessary for a single run but is good practice
    # for competitive programming problems that might have multiple test cases.
    sys.exit()

# Create a dictionary to store the word-value pairs.
dictionary = {}

# Read the 'm' words and their corresponding values.
for _ in range(m):
    word, value = input().split()
    dictionary[word] = int(value)

# Process each of the 'n' job descriptions.
for _ in range(n):
    total_salary = 0
    while True:
        try:
            line = input()
        except EOFError:
            # Handle end-of-file mid-description.
            break

        # A period on its own line signals the end of a job description.
        if line == '.':
            break
        
        # Split the line into words.
        words = line.split()
        
        # Check each word and add its value to the total salary.
        for word in words:
            # We use .get() here which is a slightly cleaner way to handle
            # missing keys, returning 0 if the word isn't in the dictionary.
            total_salary += dictionary.get(word, 0)
    
    # Print the total salary for the current job description.
    print(total_salary)

