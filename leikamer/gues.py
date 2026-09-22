high = 1000
low = 1
inp = ""

while inp != "correct":
    guess = (low+high)//2
    print(guess)
    inp = input()
    
    if inp == "higher":
        low = guess + 1

        
    if inp == "lower":
        high = guess - 1
    
