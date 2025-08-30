meters = int(input("How many meters did you travel:"))
minutes = int(input("How long did it take in minutes?:"))

kilometers = meters/1000
hours = minutes/60 

speed = kilometers/hours

print(f"You were traveling {round(speed, 2)}km/h")

#forrit sem tekur 2 inputs og printa ut hversu hratt intakið fer a km/h
