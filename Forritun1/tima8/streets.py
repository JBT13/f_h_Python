# street = " "

# list = []
# tuple = []

# while street != "q":
#     street = input()
#     list.append(street)
#     tuple.append(street)


# list.remove("q")
# tuple.remove("q")
# print(list)
# print(tuple)

list_of_addresses = []
list_of_tuples = []

while True:
    user_input = input()

    # The user types "q" to quit the loop.
    if user_input.lower() == "q":
        break
    
    # Add the full string to the first list.
    list_of_addresses.append(user_input)

    # Split the string to create the tuple.
    parts = user_input.split()
    
    # Join the street name parts in case it's a multi-word street name.
    # For example, "Old Street 123" will split into ["Old", "Street", "123"].
    # We want "Old Street" as the name, so we join all parts except the last.
    street_name = " ".join(parts[:-1])
    street_number = parts[-1]
    
    # Create the tuple and add it to the second list.
    list_of_tuples.append((street_name, street_number))

print(list_of_addresses)
print(list_of_tuples)