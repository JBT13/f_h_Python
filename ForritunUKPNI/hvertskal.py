city = input()

city_set = {"Reykjavik","Kopavogur","Hafnarfjordur",
            "Reykjanesbaer","Gardabaer","Mosfellsbaer",
            "Arborg","Akranes","Seltjarnarnes"
}

city_set1 = {"Akureyri","Fjardabyggd","Mulathing"}

if city in city_set:
    print("Reykjavik")

elif city in city_set1:
    print("Akureyri")