string = input("Enter a string to hide: ")

print(f"Your string: {string}")

while string != len(string):
    char = input("Enter a character to hide: ")
    if char in string:
        string = string.replace(char,"*",len(string))
        print(f"Your string: {string}")
    else: 
        print(f"No {char} left to hide.")
        break

# Forrit sem tekur inn streng og felur ákveðin tákn með því að nota replace aðferðina


  
  