import numpy
import matplotlib.pyplot as plt

x = [7.59, 6.28, 6.07, 5.23, 5.54, 3.46, 2.44, 3.01, 13.63, 13.02, 23.38, 9.24, 3.22,
2.06, 4.04, 17.11, 12.26, 19.91, 8.50, 7.81, 7.18, 6.95, 18.64, 7.10, 6.04, 5.66,
8.86, 4.40, 3.57, 4.35, 3.84, 2.37, 3.81, 5.32, 5.84, 2.89, 4.68, 1.85, 9.14,
8.67, 9.52, 2.68, 10.14, 9.20, 7.31, 2.09, 6.32, 6.53, 6.32, 2.01, 5.91, 5.60,
5.61, 1.50, 6.46, 5.29, 5.64, 2.07, 1.11, 3.32, 1.83, 7.56]

# Median
new = sorted(x)

if len(new) % 2 == 0:
    h = new[len(new)//2] # getting the high
    l = new[(len(new)//2)-1]
    median = (h + l)/2
    print(median)


# Mean Value
total = sum(x)
n = len(x)

answer = total/n
print(answer)

# Standard deviation Population and Sample

pstd = numpy.std(x) #Population std

sstd = numpy.std(x, ddof=1)# Sample std
print(sstd)

# Histogram
plt.hist(x, bins=8, edgecolor="black", color="skyblue") 

plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Daemi1 Histogram")
plt.show()

# Boxplot

plt.boxplot(x, vert=False, patch_artist=True)

plt.title("Daemi1 Boxplot")
plt.ylabel("Values")

plt.show()



