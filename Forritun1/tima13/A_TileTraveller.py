def main():
    """
    The main loop of the program
    """
    player = (1,1)
    while player != (3,1):
        movement(player)
        direction = input("Direction: ")
        new_player = move_player(player, direction)
        if new_player != player:
            player = new_player
    print("Victory!")

ALL_WAYS = ["N","E","S","W"]
AVAILABLE_ROUTES = {
    (1, 1): ["N"],
    (1, 2): ["N", "E", "S"],
    (1, 3): ["E", "S"],
    (2, 1): ["N"],
    (2, 2): ["S", "W"],
    (2, 3): ["E", "W"],
    (3, 1): [],          # Victory
    (3, 2): ["N", "S"],
    (3, 3): ["S", "W"],
}

def can_move(x:str, player:tuple) -> bool:
    """ Checks if the player can move

    Args:
        x (str): The direction (N E S W)
        player (tuple): The coordinates

    Returns:
        bool: True if x is a correct direction (N E S W)
    """

    if x in AVAILABLE_ROUTES[player]:
        return True
    else: return False

def movement(player: tuple) -> None:
    """ Shows the correct ways the player can travel

    Args:
        player (tuple): The coordinates
    """

    printable = []
    for i in ALL_WAYS:
        if can_move(i, player):
            if i == "N":
                printable.append(f"({i})orth")
            elif i == "E":
                printable.append(f"({i})ast")
            elif i == "S":
                printable.append(f"({i})outh")
            elif i == "W":
                printable.append(f"({i})est")

    print(f"You can travel: {' or '.join(printable)}.")


def move_player(player: tuple, direction:str) -> tuple:
    """ Moves the player according to the direction given

    Args:
        player (tuple): The players coordinates
        direction (str): A direction that will be checked if valid

    Returns:
        tuple: The new location of the player
    """


    valid = "NSWE"
    direction = direction.upper()
    
    if direction not in valid:
        print("Not a valid direction!")
        return player
    
    if not can_move(direction,player):
        print("Not a valid direction!")
        return player

    x, y = player
    if direction == "N":
        y += 1
    elif direction == "S":
        y -= 1
    elif direction == "E":
        x += 1
    elif direction == "W":
        x -= 1
    return (x, y)



if __name__ == "__main__":
    main()