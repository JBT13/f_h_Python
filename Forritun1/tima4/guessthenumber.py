low = 1
high = 1000
guess = (low + high) // 2

print(guess)

while n != "correct":
    n = input()

    if n == "higher":
        low = guess + 1
    elif n == "lower":
        high = guess - 1

    guess = (low + high) // 2
    print(guess)
