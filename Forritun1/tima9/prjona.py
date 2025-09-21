# a, b = map(int, input().split())

# count = {
#     "." : 20,
#     "O" : 10,
#     "\\" : 25,
#     "/" : 25,
#     "A" : 35,
#     "^" : 5,
#     "v" : 22
# }

# teljari = []
# for _ in range(a):
#     entry = input()
#     name, points = entry.split()
#     points = int(points)

#     if name in scores:
#         scores[name] += points
#     else:
#         scores[name] = points
# print(teljari)
        


# Get the dimensions of the grid
a, b = map(int, input().split())
# Define the point values for each character
count = {
    "." : 20,
    "O" : 10,
    "\\" : 25,
    "/" : 25,
    "A" : 35,
    "^" : 5,
    "v" : 22
}

# Initialize the total score
total_points = 0

# Read the grid and calculate the total points
for _ in range(a):
    row_input = input()    
    for char in row_input:
        if char in count:
            total_points += count[char]
        else:
            # Handle unrecognized characters gracefully
            print(f"Warning: Unrecognized character '{char}' in input.")

# Print the final score
print(total_points)

