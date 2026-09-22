import numpy
import matplotlib.pyplot as plt

x = [-0.3, 3.1, 3.1, 5.7, 9.0, 8.8, 12.1, 11.9, 9.2, 4.7, 1.9, 4.0]

medaltal = sum(x)/len(x) # Medaltal

pstd = numpy.std(x) #Population std

sstd = numpy.std(x, ddof=1)# Sample std

print(f"Meðaltal {medaltal}")
print(f"Staðalfrávik {sstd}")
print(f"Talnabilið {medaltal-sstd}, {medaltal+sstd}")

print(sorted(x))
print(len(x))

# Histogram   start -2 til 14.6, step 1.5
bin = numpy.arange(-2, 14.6, 1.5)

plt.hist(x, bins=bin, edgecolor="black", color="skyblue") 

plt.xlabel("Hitastig")
plt.ylabel("Frequency")
plt.title("Ass1 Histogram")
plt.show()

# Boxplot 
q1 = 3.1
q2 = 5.2
q3 = 9.1

plt.figure(figsize=(8, 4))
plt.boxplot(x, vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))

# Labeling Q1, Median, and Q3 on the graph
plt.text(q1, 1.15, f'Q1: {q1}', horizontalalignment='center', fontweight='bold', color='blue')
plt.text(q2, 1.15, f'Miðgildi: {q2}', horizontalalignment='center', fontweight='bold', color='red')
plt.text(q3, 1.15, f'Q3: {q3}', horizontalalignment='center', fontweight='bold', color='blue')

plt.title("Boxgraf af hitastigsgögnum")
plt.xlabel("Hitastig (°C)")
plt.yticks([]) 
plt.ylim(0.7, 1.3) # make space for text
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.show()