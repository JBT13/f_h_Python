side1 = int(input("Enter in the first side of the triangle: "))
side2 = int(input("Enter in the second side of the triangle: "))
side3 = int(input("Enter in the third side of the triangle: "))

if side1 == side2 and side2 == side3 and side1== side3:
  print("This is a equilateral triangle")

elif side1 == side2 or side2 == side3 or side1== side3:
  print("This is an isoceles triangle")

else: 
  print("This is a scalene triangle")
  
#tjekka hva type af triangles
