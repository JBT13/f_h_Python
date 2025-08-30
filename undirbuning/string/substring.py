string = input("Enter in a string: ")
substring = input("What substring do you want to check?: ")

if substring in string:
  print(f"{substring} is a substring of {string}")

elif not substring in string:
  print(f"There is no {substring} in {string}")

#tjekka hvort string 2 er a substring of string 1 með því að nota aðferðin "IN"