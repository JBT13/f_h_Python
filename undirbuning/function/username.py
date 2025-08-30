def is_valid_name(name):
    name_parts = name.split()
    if all(part.isalpha() for part in name_parts) and len(name_parts) >= 2:
        return True
    else:
        print("Invalid name!")
        return False
def is_valid_year(year):
    if year.isdigit():
        year_int = int(year)
        return 1900 < year_int < 2025
    else:
        print("Invalid year!")
        return False

def generate_username(name, year):
    if is_valid_name(name) and is_valid_year(year):
        name_parts = name.split()
        first_name = name_parts[0]
        initials = ''.join(part[0].lower() for part in name_parts[1:])
        username = first_name + initials + year[-2:]
        return username
    else:
        return "Invalid input. Please enter a valid name and year."

name_input = input("Enter in your name: ")
year_input = input("Enter in your date of birth: ")

username = generate_username(name_input, year_input)
print("Your new username:", username)
