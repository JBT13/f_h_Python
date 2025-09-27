length = 10
charX = 'x'
position = 'o'

def get_initial_position():
    number = 0
    # Loop until the number is 1-10
    while number < 1 or number > length:
        # NOTE 1: Added a newline character to the prompt to prevent TLE.
        # NOTE 2: Input is stripped of whitespace to handle unexpected user input.
        user_input = input(f"Position in [1..{length}]:\n").strip() 
        
        # Check if the input is a valid digit string
        if user_input.isdigit():
            number = int(user_input)
            
        else:
            number = 0 
            
    return number - 1 

def generate_display(current_index):

    list_o_x = [charX] * length
    list_o_x[current_index] = position

    return "".join(list_o_x)

def run_game():
    
    current_index = get_initial_position()
    
    command = '' 
    
    # We enter the loop immediately to display the initial position
    # and then check the command condition at the start of the next cycle.
    
    # Start loop flag
    is_first_move = True

    while command != 'q': 
        
        # We only display the board and options AFTER a move, 
        # and only display the board ONCE for the initial state.
        if not is_first_move:
            print(generate_display(current_index))
            print("l: left")
            print("r: right")
            
            # This is where the movement prompt happens
            command = input("Move: ").lower()
        
        # Special logic to display the initial board once, and then immediately ask for the first move command
        if is_first_move:
            current_view = generate_display(current_index)
            print(current_view)
            print("l: left")
            print("r: right")
            command = input("Move: ").lower()
            is_first_move = False
            
        
        # Check for exit commands *first*
        if command == 'q':
            # Loop condition will terminate the game after this iteration.
            continue
        
        # Apply movement logic with boundary checks
        new_index = current_index 
        
        if command == 'r':
            if current_index < length - 1:
                new_index += 1
        
        elif command == 'l': 
            if current_index > 0:
                new_index -= 1
                
        # If the command is not 'r' or 'l', new_index remains current_index.

        # Update the index for the next turn
        current_index = new_index

# --- Note on execution ---
if __name__ == "__main__":
    run_game()