# Read the dimensions of the grid from the first line of input
rows, columns = map(int, input().split())

# Read the grid data
grid = []
for _ in range(rows):
    row_data = list(map(int, input().split()))
    grid.append(row_data)

found = False

# Iterate through the inner numbers of the grid, skipping the outer border
for r in range(1, rows - 1):
    for c in range(1, columns - 1):
        current_number = grid[r][c]
        
        # Check if the current number is smaller than all of its neighbors
        if (current_number < grid[r - 1][c] and
            current_number < grid[r + 1][c] and
            current_number < grid[r][c - 1] and
            current_number < grid[r][c + 1]):
            found = True
            # Stop checking as soon as a match is found
            break
    if found:
        break

# Print the final result
if found:
    print("Jebb")
else:
    print("Neibb")
