def not_valid(position_func):
    print("Not a valid direction!")
    position_func()

def position_1_1():
    print("You can travel: (N)orth.")
    direction = input("Direction: ")
    if direction.lower() == "n":
        position_1_2()
    else:
        not_valid(position_1_1)
    
def position_1_2():
    print("You can travel: (N)orth or (E)ast or (S)outh.")
    direction = input("Direction: ")
    if direction.lower() == "n":
        position_1_3()
    elif direction.lower() == "e":
        position_2_2()
    elif direction.lower() == "s":
        position_1_1()
    else:
        not_valid(position_1_2)

def position_1_3():
    print("You can travel: (E)ast or (S)outh.")
    direction = input("Direction: ")
    if direction.lower() == "e":
        position_2_3()
    elif direction.lower() == "s":
        position_1_2()
    else:
        not_valid(position_1_3)

def position_2_1():
    print("You can travel: (N)orth.")
    direction = input("Direction: ")
    if direction.lower() == "n":
        position_2_2()
    else:
        not_valid(position_2_1)


def position_2_2():
    print("You can travel: (S)outh or (W)est.")
    direction = input("Direction: ")
    if direction.lower() == "w":
        position_1_2()
    elif direction.lower() == "s":
        position_2_1()
    else:
        not_valid(position_2_2)

    
def position_2_3():
    print("You can travel: (E)ast or (W)est.")
    direction = input("Direction: ")
    if direction.lower() == "e":
        position_3_3()
    elif direction.lower() == "w":
        position_1_3()
    else:
        not_valid(position_2_3)

def position_3_1():
    print("Victory!")

def position_3_2():
    print("You can travel: (N)orth or (S)outh.")
    direction = input("Direction: ")
    if direction.lower() == "s":
        position_3_1()
    elif direction.lower() == "n":
        position_3_3()
    else:
        not_valid(position_3_2)
    
def position_3_3():
    print("You can travel: (S)outh or (W)est.")
    direction = input("Direction: ")
    if direction.lower() == "s":
        position_3_2()
    elif direction.lower() == "w":
        position_2_3()
    else:
        not_valid(position_3_3)

position_1_1()