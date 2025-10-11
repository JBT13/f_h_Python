def get_name():
    user = input("What's your name?\n")
    alpha_user = user
    if " " in user:
       alpha_user = user.replace(" ", "")
    while not alpha_user.isalpha():
        print("Please enter a valid name.")
        user = get_name()
        alpha_user = user.replace(" ", "")

    return user 

def is_int(string1):
    try:
        int(string1)
    except:
        return False
    
    return True

def get_age():
    age = input("How old are you?\n")
    if is_int(age):
        int_age = int(age)
        while int_age < 0 or int_age > 125:
            print(f"You seriously expect me to believe you are {age} years old?")
            age = get_age()
            int_age = int(age)

    while not is_int(age):
        print("Please enter an integer.")
        age = get_age()

    return age

name = get_name()
age = get_age()

print(f"Nice to meet you {name}.") 
print(f"Congratulations on your {age} years.")   
