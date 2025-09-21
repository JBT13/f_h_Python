# First, get the number of knights.
num_knights = int(input())

# This list will store the details for each knight: [original_row_number, health, strength].
knights = []
# Loop to get the health and strength for each knight.
for i in range(num_knights):
    h, s = map(int, input().split())
    # Store the knight's original row number, health, and strength.
    knights.append([i + 1, h, s])

# The tournament loop continues as long as there is more than one knight.
while len(knights) > 1:
    # This list will hold the winners of the current round.
    winners = []
    
    # Process the knights in pairs.
    i = 0
    while i < len(knights):
        knight1 = knights[i]
        
        # Check if there is a second knight to fight. If not, the last knight gets a 'bye'.
        if i + 1 < len(knights):
            knight2 = knights[i + 1]
            
            # This inner loop represents a single battle, turn by turn.
            while knight1[1] > 0 and knight2[1] > 0:
                # Knight 1 attacks Knight 2.
                knight2[1] = knight2[1] - knight1[2]
                
                # Check if Knight 2 is defeated after the attack.
                if knight2[1] <= 0:
                    break  # End the battle
                
                # Knight 2 attacks Knight 1.
                knight1[1] = knight1[1] - knight2[2]

            # After the battle ends, determine the winner and add them to the winners list.
            if knight1[1] > 0:
                winners.append(knight1)
            else:
                winners.append(knight2)
        
        else:
            # If there's an odd number of knights, the last one gets a 'bye' and moves on.
            winners.append(knight1)

        # Move to the next pair of knights.
        i = i + 2
    
    # The winners of this round become the fighters for the next round.
    knights = winners

# Once only one knight remains, print their original row number.
print(knights[0][0])