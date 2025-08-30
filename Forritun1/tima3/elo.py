elo = int(input())

if elo <= 999:
    print("Invalid")

elif elo < 2400:
    print("Amateur")

elif elo >= 2400 and elo < 2500:
    print("International grandmaster")

elif elo >= 2500 and elo <=2699:
    print("Grandmaster")

elif elo >= 2700:
    print("Super grandmaster")

