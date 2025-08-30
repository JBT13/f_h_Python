user_input = input("Enter an integer: ")

try:
    number = int(user_input)

    if number <= 0:
        print("Vinsamlegast sláðu inn jákvæða heiltölu.")
    else:
        i = 1
        while i ** 2 <= number:
            print(i ** 2)  # Annað veldi af i
            i += 1
except ValueError:
    print("Þetta er ekki gild heiltala.")

#tekur á móti talan forrit á siðan að sýna alla square root sem eru minna eða jafn og talan
# td 17 = 16,9,4,1 

