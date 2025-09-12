# Write code below 💖
gry = 0
rave = 0
huff = 0
sly = 0


print("     1) Dawn")
print("     2) Dusk")
q1 = int(input("Q1) Do you like Dawn or Dusk? "))


if q1 == 1:
  gry =+ 1
  rave =+ 1

elif q1 == 2:
  huff =+ 1
  sly =+ 1

else:
  print("Wrong Input")

print("     1) The Good")
print("     2) The Great")
print("     3) The Wise")
print("     4) The Bold")
q2 = int(input("Q2) When I'm dead, I want people to remember me as: "))


if q2 == 1:
  huff =+ 2

elif q2 == 2:
   sly =+ 2

elif q2 == 3:
  rave =+ 2

elif q2 == 4:
  gry =+ 2

else:
  print("Wrong input.")

print("     1) The violin")
print("     2) The trumpet")
print("     3) The Piano")
print("     4) The drum")
q3 = int(input("Q3) Which kind of instrument most pleases your ear? "))

if q3 == 1:
  sly =+ 4

elif q3 == 2:
  huff =+ 4

elif q3 == 3:
  rave =+ 4

elif q3 == 4:
  gry =+ 4

else:
  print("Wrong input.")

  
print("Gryffindor: ", gry)
print("Ravenclaw: ", rave)
print("Hufflepuff: ", huff)
print("Slytherin: ", sly)





