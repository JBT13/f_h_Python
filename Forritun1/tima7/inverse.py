s = input()

for ch in s:  # for characters in sentences 
    ascii = ord(ch) # ord the characters turn the i / letters into numbers 
    if 65 <= ascii <= 90:  # A–Z 
        print(chr(ascii + 32), end="") #+32 ascii table 
    elif 97 <= ascii <= 122:  # a–z
        print(chr(ascii - 32), end="") #-32 ascii table
    else:
        print(ch, end="") # dont change spaces ? "" etc