# ammount = int(input())

# movies = input()

# movies_list = movies.split()

# #Convert each string in the list to an integer
# # This creates a new list with the numbers as integers
# movie_list = [int(x) for x in movies_list]

# movie_list.sort()

# section_size = ammount // 3

# # Get the three parts of the list using the dynamic section_size
# middle_movies = movies_list[section_size:section_size * 2]
# first_movies = movies_list[0:section_size]
# last_movies = movies_list[section_size * 2:section_size * 3]

# movie_list.sort()

# # Combine the lists in the new order: middle, first, last
# reordered = middle_movies + first_movies + last_movies

# # Print the final list with each number separated by a space
# print(*reordered)

# Read the total number of items
amount = int(input())

# Read the second line of input as a single string
input_str = input()

# Split the string of numbers into a list of strings
list_str = input_str.split()

# Convert each string in the list to an integer
numbers_list = [int(x) for x in list_str]

# Step 1: Sort the list in ascending order
numbers_list.sort()

# The logic is based on dividing the list into three sections.
# Since the amount is always a multiple of 3, we can use integer division.
section_size = len(numbers_list) // 3

# Step 2: Extract the three sections using slicing
# We use the sorted list for this step.
first_section = numbers_list[0:section_size]
middle_section = numbers_list[section_size:section_size * 2]
last_section = numbers_list[section_size * 2:]

# Step 3: Combine the sections in the desired order
# The pattern is middle, then first, then last
reordered_list = middle_section + first_section + last_section

# Print the final list with each number separated by a space
print(*reordered_list)