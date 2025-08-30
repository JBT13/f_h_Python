import random

number_to_guess = random.randint(1, 100)

num = int(input("Guess a number in the range 1-100: "))

while number_to_guess < 100:
    
  if num == number_to_guess:
    print(f"You are correct, the number was {number_to_guess}!")
    break
  
  elif num < number_to_guess:
    print(f"The number is larger")
    num = int(input("Guess a number in the range 1-100: "))
  
  elif num > number_to_guess:
    print(f"The number is smaller")
    num = int(input("Guess a number in the range 1-100: "))

# guess the number cant be simpler
# byrjaðu með 50 og svo half og svo og svo