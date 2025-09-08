value = int(input("Enter a number: "))

print("\n🔍 Brute-force method (1 to value):")
brute_count = 0
for i in range(1, value + 1):
    if value % i == 0:
        print(f"Divisor found: {i}")
        brute_count += 1
print(f"Total divisors (brute-force): {brute_count}")
