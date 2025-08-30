sentence = input("Enter in a sentence: ")

num_of_digits = sum(c.isdigit() for c in sentence)
num_of_characters = sum(c.isalpha() for c in sentence)
num_of_upper = sum(c.isupper() for c in sentence)
num_of_lower = sum(c.islower() for c in sentence)

print(f"The input has {num_of_digits} digits and {num_of_characters} alphabetic characters "
      f"where {num_of_upper} are upper case and {num_of_lower} are lower case.")
