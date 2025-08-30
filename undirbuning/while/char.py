char = 0
final = ""

while char != "done":
    char = str(input("Enter a single character to add to string: "))
    if char != "done" and len(char) > 1:
        print(f"Input must be a single character")
    elif len(char) == 1:
        final += char 

print(f"{final}")

        


