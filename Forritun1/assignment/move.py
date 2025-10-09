"""
a simple game where a character 'o' moves left or right 
on a line of 10 x 
"""

LENGTH = 10
CHAR_X = 'x'
POSITION = 'o'

def get_initial_position():
    """ here we are getting our number to put it on the list later on """

    number = 0
    while number < 1 or number > LENGTH: 
        
        user_input = input(f"Position in [1..10]: ") 
        
        if user_input.isdigit(): #paranoia from tima12 daemi 4
            number = int(user_input) 
            
        else:
            number = 0 
            
    return number - 1  # Here is -1 for the index otherwise we would start +1 

def generate_grid(current_index): 
    """ here we are creating the list of x with o """ 

    list_o_x = [CHAR_X] * LENGTH # here we are at xxxxxxxxxx
    list_o_x[current_index] = POSITION # here we append o into the x

    return "".join(list_o_x) 

def run_game():
    """ here we are running the game"""

    current_index = get_initial_position() # call our function to get the number
    
    command = 'r'

    while command == "r" or command == "l": 
        
        current_view = generate_grid(current_index) 
        print(current_view)
        print("l: left")
        print("r: right")
        command = input("Move: ").lower() 
        #if input != r or q , we dipping GG (GOOD GAME)

        new_index = current_index 
        
        if command == 'r':
            # we move right unless we are at 10 (index 9)
            if current_index < LENGTH - 1: 
                #no -1 we are fried (the -1 is so that we dont go "outta bounds") 
                new_index += 1  
        
        elif command == 'l': 
            # we move left unless we are at 1 (index 0)
            if current_index > 0: # no problem here cause 0 not > 0
                new_index -= 1 
                
        current_index = new_index 
        #update position

if __name__ == "__main__":
    run_game()