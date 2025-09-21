letters = input()

#Geymum the ammount of mðguleikar hér 
possibilities = []
i = 0
while i < len(letters):
    j = i # þannig ég fer ekki ofar í the same gaur
    while j < len(letters):
        possibilities.append(letters[i:j+1]) 
        j += 1
    i += 1 
    
# dictionary fyrir the ammount of times fyrir hver möguleika
counts = {}
for posible in possibilities:
    if posible in counts:
        counts[posible] += 1 #+1 if the gaur kemur meira en einu sinni
    else:
        counts[posible] = 1 #annars 1 

# Sort alphabetically.
order_letters = list(counts.keys())

# Sort by the count in descending order (AI got me here got no clue about the 3 A 2 T) 
order_letters.sort(key=lambda x: (-counts[x], x))


for posible in order_letters:
    print(f"{counts[posible]} {posible}")
