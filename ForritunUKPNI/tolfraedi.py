import sys
from collections import Counter

# Set a high recursion limit for safety, though not strictly needed here
# sys.setrecursionlimit(2000)

def solve():
    # Read the number of changes
    try:
        # Read the first line (n)
        n = int(sys.stdin.readline())
    except:
        # Handle empty input case
        return

    # Use a Counter to track the frequency of each age. This is key for O(1) removals.
    ages_count = Counter()
    
    # Use a set to track the unique ages. This makes finding the min/max keys faster 
    # when the current min/max is removed.
    unique_ages = set()
    
    current_sum = 0
    total_suitors = 0
    current_min = -1
    current_max = -1

    for _ in range(n):
        # Read the action line (e.g., "A 2", "R 5")
        try:
            line = sys.stdin.readline().split()
            if not line:
                continue
            action = line[0]
            age = int(line[1])
        except:
            continue
        
        # --- ADD (A) Operation ---
        if action == "A":
            # Update counts and sum
            ages_count[age] += 1
            unique_ages.add(age)
            current_sum += age
            total_suitors += 1
            
            # O(1) Min/Max Update
            if total_suitors == 1: # First element added
                current_min = age
                current_max = age
            else:
                if age < current_min:
                    current_min = age
                if age > current_max:
                    current_max = age
                    
        # --- REMOVE (R) Operation ---
        elif action == "R":
            # Check if the suitor (with this age) actually exists to be removed
            if ages_count[age] > 0:
                # Update counts and sum
                ages_count[age] -= 1
                current_sum -= age
                total_suitors -= 1
                
                # Check if the age count dropped to zero
                if ages_count[age] == 0:
                    unique_ages.remove(age) # Remove from the set of unique ages
                
                # O(1) Min/Max Check: Only recalculate if the removed age 
                # was the current min OR max AND its count hit zero.
                
                # If we removed the current minimum and its count is now 0, we must find the new minimum.
                # The minimum of a set/dictionary keys is a relatively fast operation, 
                # but technically O(U) where U is the number of unique ages.
                if total_suitors > 0:
                    if age == current_min and ages_count[age] == 0:
                        # Find the new min (The min of the keys remaining in the set)
                        current_min = min(unique_ages) 
                    
                    # If we removed the current maximum and its count is now 0, we must find the new maximum.
                    if age == current_max and ages_count[age] == 0:
                        # Find the new max (The max of the keys remaining in the set)
                        current_max = max(unique_ages) 
                
        # --- OUTPUT ---
        if total_suitors == 0:
            print("-1 -1 -1")
            # Reset min/max trackers
            current_min = -1
            current_max = -1
        else:
            average = current_sum / total_suitors
            # Print with high precision (as requested by the problem statement)
            print(f"{current_min} {current_max} {average:.6f}")


# Run the function
solve()


# n = int(input())

# numbers = []

# for _ in range(n):
#     action = input()
#     if action[0] == "A":
#         action = int(action[2:])
#         numbers.append(action)
#         numbers = list(map(int, numbers))
#         print(min(numbers), max(numbers), sum(numbers)/len(numbers))
#     elif action[0] == "R":
#         action = int(action[2:])
#         numbers.remove(action)
#         numbers = list(map(int, numbers))
#         print(min(numbers), max(numbers), sum(numbers)/len(numbers))

