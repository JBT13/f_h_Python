# from itertools import zip_longest

# # n = int(input())

# # if n == 1:
# #     a = input()
# #     for i in a:
# #         print(i)

# # else:
# #     words = []
# #     for _ in range(n):
# #         a = input()
# #         words.append(a)

# #     for chars_tuple in zip_longest(*words, fillvalue=""):
# #         for char in chars_tuple:
# #             if char:
# #                 print(char, end="")

# #         print()

from itertools import zip_longest
import sys

def interleave_strings_from_user():
    # 1. Ask user for the number of strings (n)
    while True:
        try:
            # Read n from user input
            n_str = input().strip()
            n = int(n_str)
            if n > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # 2. Ask user for the n strings/lines and store them
    words = []
    for _ in range(n):
        # Using input() for interactive prompts
        line = input()
        words.append(line)

    # If there are no words, stop.
    if not words:
        return

    # 3. Find the maximum length and pad all lines
    # This is CRUCIAL for preserving the column structure and spaces!
    max_len = max(len(word) for word in words)

    # Pad every word with spaces on the right to match max_len
    padded_words = [word.ljust(max_len) for word in words]

    # 4. Interleave the padded lines column by column
    # Using None as the fillvalue is safest, though not strictly needed 
    # since we've already padded all lines to the max length.
    for chars_tuple in zip_longest(*padded_words, fillvalue=None):
        # Join all characters, filtering only the None placeholder.
        # This PRESERVES ALL SPACES from the padded input.
        line = "".join(char for char in chars_tuple if char is not None)

        # Print the resulting column on a new line
        print(line)

# Execute the function
if __name__ == "__main__":
    interleave_strings_from_user()

