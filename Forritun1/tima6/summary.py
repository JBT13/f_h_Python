import math

count = 0
avg = 0
m = 0

while True:
    n = int(input())
    if n == -1:
        break

    count += 1
    delta = n - avg   # Measures how far the new value is from the current average.
    avg += delta / count # updates the average , the more values (count), the smaller the adjustment
    delta2 = n - avg  # re measure how far the new value is from the new average
    m += delta * delta2 # updates the running total of squared differences 

    variance = m / count # population variance 

    std_deviation = math.sqrt(variance) # standart population deviation 

    print(f"{avg:.2f}")
    print(f"{std_deviation:.2f}")