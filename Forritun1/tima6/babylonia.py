number = int(input())
guess = int(input())
tolerance = float(input())

count = 0
past_guess = 0

while abs(guess - past_guess) > tolerance:
    past_guess = guess
    guess = (guess + number / guess) / 2
    count += 1

print(f"{guess:.4f}")
print(count)