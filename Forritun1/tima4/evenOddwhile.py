n = int(input()) # gets the input 

while n != 1: # while n is not 1 it should run
    print(n) # we print the first input

    if n % 2 == 0:  # if the input is even then 
        n = n // 2 # we assign our new n its (the old n // 2)  
    else: # if its odd then
        n = n * 3 + 1 # we assign our new n its (the old n * 3 +1)
    
print(n) # we print out our new n 
