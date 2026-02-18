a = input()

vowels = {"a": 0, "e": 0, "i": 0, "o":0, "u":0}
count = 0

for i in range(len(a)):
    if "r" == a[i]:
        count += 1

    if a[i] in vowels:
        vowels[a[i]] += 1


flagg = False
if count >= 2 and a[0] == "b" and a[-1] in vowels:
    flagg = True

flagg1 = False
for key, value in vowels.items():
    if value == 1:
        flagg1 = True

if flagg and flagg1:
    print("Jebb")

else:
    print("Neibb")         
