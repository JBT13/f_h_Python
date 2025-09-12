name = input()

last, first = name.split(", ")

firstName = first.strip().capitalize()
LastName = last.strip().capitalize()

print(f"{firstName[0]}. {LastName}")