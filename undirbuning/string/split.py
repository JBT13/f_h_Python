sentence = input("Enter in sentence: ")
words = sentence.split(" ")  # split the words þannig forrit getur recognise which one eru "orð"
swapped_words = [] # bua til list 

for word in words:
   if len(word)> 1: # þannig þa kemur ekki "aa" ef það er bara "a" 
      swapped = word[-1] + word[1:-1] + word[0] # position til að swappea 
   else:
      swapped = word
   swapped_words.append(swapped) #" append the words = setja í the list eftir buinn að swapped"

print(" ".join(swapped_words)) # join the words aftur saman með space join = glue með words 


    
