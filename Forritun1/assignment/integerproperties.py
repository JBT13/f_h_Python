import math

# Part 1: Check for 10 or more positive divisors 
while True:
    user_input = input()
    if user_input.lower() == "q":
        break

    value = int(user_input)
    count = 0

    for i in range(1, int(math.sqrt(value)) + 1):
        if value % i == 0:
            count += 1
            if i != value // i:
                count += 1
        if count >= 10:
            break

    print("yes" if count >= 10 else "no")

# Part 2: Read final number after "q"
final_number = int(input())

# Two-digit numbers: digit sum squared equals number
for number in range(10, min(final_number + 1, 100)):
    digit_sum = sum(int(d) for d in str(number))
    if digit_sum ** 2 == number:
        print(number)

# Three-digit numbers: digit sum cubed equals number
for number in range(100, min(final_number + 1, 1000)):
    digit_sum = sum(int(d) for d in str(number))
    if digit_sum ** 3 == number:
        print(number)