import math

n = input()

while n.lower() != "q":
    n_int = int(n)
    count = 0

    for i in range(1, int(math.sqrt(n_int)) + 1):
        if n_int % i == 0:
            count += 1
            if i != n_int // i:
                count += 1
        if count >= 10:
            break
    
    if count >= 10:
        print(f"yes")

    else:
        print(f"no")

    n = input()


if n == "q":
    n = int(input())
    two_digit_results = []
        # Two-digit numbers range from 10 to 99. We check up to n.
    for number in range(10, min(n + 1, 100)):
            # Convert the number to a string to access its digits.
        digits = str(number)
            
            # Calculate the sum of the digits.
        digit_sum = int(digits[0]) + int(digits[1])
            
            # Check if the square of the digit sum equals the number.
        if digit_sum ** 2 == number:
                two_digit_results.append(number)
        
        # Display the results for two-digit numbers.
    if two_digit_results:
        for num in two_digit_results:
            print(num)
            
        # 2. Check for three-digit numbers
    three_digit_results = []
        # Three-digit numbers range from 100 to 999. We check up to n.
    for number in range(100, min(n + 1, 1000)):
            # Convert the number to a string to access its digits.
        digits = str(number)
            
            # Calculate the sum of the digits.
        digit_sum = int(digits[0]) + int(digits[1]) + int(digits[2])
            
            # Check if the cube of the digit sum equals the number.
        if digit_sum ** 3 == number:
            three_digit_results.append(number)
        
        # Display the results for three-digit numbers.
    if three_digit_results:
        for num in three_digit_results:
            print(num)


