low = 1
high = 1000
guess = (low + high) // 2

print(guess)

while True:
    n = input()

    if n == "higher":
        low = guess + 1
    elif n == "lower":
        high = guess - 1
    elif n == "correct":
        break

    guess = (low + high) // 2
    print(guess)
