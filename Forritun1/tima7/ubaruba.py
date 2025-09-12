trande = input()  # 'D' triggers the transformation
lines = int(input())  # Number of lines to process

vowels = ("aeiouy")
count = 0
trans = []    

while count < lines:
    sentence = input()
    output = ""
    if trande == "D":
        for char in sentence:
            if char.lower() in vowels:
                output += "ub" + char
            else:
                output += char
    elif trande == "A":
        i = 0 
        while i < len(sentence):   
            if (sentence[i:i+2].lower() == "ub") and i+2 < len(sentence) and sentence[i+2].lower() in vowels:
                output += sentence[i+2]
                i += 3
            else:
                output += sentence[i]
                i += 1 

    trans.append(output)
    print(output)
    count += 1

