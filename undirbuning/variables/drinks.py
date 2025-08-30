pakka = int(input("How big is the drink pack?:"))
drinks = int(input("How many are you going to buy?:"))

amount_of_packs = drinks // pakka 
seperate_drinks = drinks % pakka

print(f"You have to buy {amount_of_packs} packs and {seperate_drinks} seperate")

#tekur á moti 2 inputs og sé hversu many packs þarftu og hversu many seperate
# notar modulo til að tjekka the package 
