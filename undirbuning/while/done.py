total_sum = 0

while True:
    user_input = input('Enter a number (or "done"): ')
    
    if user_input.lower() == 'done':
        break  
    
    elif user_input:
        number = user_input  
        total_sum += number        
    else:
        print("Þetta er ekki gilt númer, reyndu aftur.")  

print(f"The sum is {total_sum}")

#forrit geymir summuna fra notandi og keyrir það þegar notandi skrifa done
