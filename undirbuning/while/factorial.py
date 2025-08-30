# Lesa inn jákvæða heiltölu
n = int(input("Enter a positive integer:\n"))

# Upphafsgildi fyrir aðfeldið
factorial = 1
i = 1

# Reikna aðfeldið með while lykkju
while i <= n:
    factorial *= i
    i += 1

# Prenta niðurstöðuna
print(f"{n}! is {factorial}")
