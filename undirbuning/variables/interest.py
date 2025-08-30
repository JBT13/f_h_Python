b = int(input("Enter in initial amount:"))
v = int(input("Enter in interest in %:"))
t = int(input("Enter in years:"))

interest = v/100 + 1

result = b*interest**t

print(f"Your investment in {t} years will be {result}kr")

#Tekur amount og bætir vextir in years