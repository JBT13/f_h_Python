r, g, b = map(int, input().split(" "))

if r > g and r > b:
    print("raudur")

elif g > r and g > b:
    print("graenn")

elif b > r and b > g:
    print("blar")

elif (r == g) and  r > b and g > b:
    print("gulur")

elif (r == b) and r > g and b > g :
    print("fjolubleikur") 

elif (g == b) and g > r and b > r:
    print("blagraenn")

elif g == 0 and b == 0 and r == 0:
    print("svartur")

elif g == 255 and b == 255 and r == 255:
    print("hvitur")

elif g == r and r == b and b == g:
    print("grar")