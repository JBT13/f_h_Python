# Function to check if a year is a leap year
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Function to efficiently count leap years up to a given year
def count_leaps_up_to(year):
    return year // 4 - year // 100 + year // 400

# The input year
n = int(input())

# Check if n is a leap year as per your logic
if not is_leap(n):
    print("Neibb")
else:
    # If n is a leap year, calculate the number of leap years
    # from 2020 up to n (exclusive of n).
    # We count leaps up to (n-1) and subtract leaps up to (2019).
    count = count_leaps_up_to(n - 1) - count_leaps_up_to(2019)
    print(count)