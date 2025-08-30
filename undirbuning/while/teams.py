team1 = input("Enter the home team's name: ")
team2 = input("Enter the away team's name: ")

team1_score = 0
team2_score = 0 

scored = input("What team scored?: ")

while scored != "done": 
    if team1 == scored:
        team1_score += 1

    elif team2 == scored:
        team2_score += 1 

    else:
        print("That team is not playing, try again")
    scored = input("What team scored?: ")

if scored == "done" and (team1_score) > (team2_score):
    print(f"{team1} won {team1_score}-{team2_score}")

elif scored == "done" and (team2_score) > (team1_score):
    print(f"{team2} won {team2_score}-{team1_score} ")

elif team1_score == team2_score:
    print(f"It's a draw {team1_score}-{team2_score}")


    