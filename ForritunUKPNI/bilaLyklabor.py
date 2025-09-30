s = input()
result = []

for char in s:
    # Check if the result list is NOT empty AND 
    # the current character is the same as the LAST character in 'result'
    if result and char == result[-1]:
        # If they are the same, pop (remove) the last character from 'result'
        # This effectively removes the adjacent pair
        continue
    else:
        # If they are different, append the current character
        result.append(char)

print("".join(result))