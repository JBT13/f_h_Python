import sys
input = sys.stdin.read

def vocales(word):
    text = ""
    text += word + "yay"
    return text 

def consonates(word):
    text = ""

    num = 0
    for index, letter in enumerate(word):
            if letter in "aeiouy":
                new_word = word[index:]
                text += new_word
                num = index
                break 
    
    text += word[0:num]
    text += "ay"

    return text 
    

b = input().strip()

texti = []

for word in b.split():
    if word[0] in "aeiouy":
        texti.append(vocales(word))

    else:
        texti.append(consonates(word))

print(" ".join(texti))

