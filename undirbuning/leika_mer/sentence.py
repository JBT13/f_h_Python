n = int(input())

# Create an empty list to store the results
capitalized_sentences = []

# This loop runs 'n' times to get all the sentences
for _ in range(n):
    s = input()
    
    if s:
        # Capitalize the first letter
        first_letter = s[0].upper()
        rest_of_sentence = s[1:].lower()
        
        # Add the new sentence to our list
        capitalized_sentences.append(first_letter + rest_of_sentence)

# Now, print all the sentences stored in the list
for sentence in capitalized_sentences:
    print(sentence)