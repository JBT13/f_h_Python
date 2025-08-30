a = int(input("Enter a: "))  # Do not remove this line
b = int(input("Enter b: "))  # Do not remove this line
c = int(input("Enter c: "))  # Do not remove this line

# Enter your solution below

d = b*b - 4 *a*c

if d > 0 :
  num = 2 
  print(f"The equation has {num} roots ")

elif d == 0 :
  num = 1 
  print(f"The equation has {num} root ")

if d < 0 :
  num = 0 
  print(f"The equation has {num} roots ")

# tjekkar hversur margar rætur er dæmi með