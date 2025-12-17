# f = 0
# f1 = 1
# n = 10 # Let's find the 10th number (counting from f0=0)

# # The correct update is: f, f1 = f1, f + f1

# for i in range(n+1):
#     # This correctly finds the next number and updates the previous two
#     f_old = f1  # Temporarily store the current f1
#     f1 = f + f1 # The new f1 is the sum
#     f = f_old   # The new f is the old f1

# print(f1 - 1) 

class Height:
    def __init__(self, feet, inches):
        self.feet = feet + int(inches / 12)
        self.inches = inches % 12

    def __str__(self):
        return f"{self.feet}ft,{self.inches} in "
    
    def cm(self):
        return f"{round(self.feet * 30.48 + self.inches * 2.54)}cm"
      
    def __gt__(self, other):
        return self.cm() > other.cm()

    def __add__(self, other):
        return Height(self.feet + other.feet, self.inches + other.inches)    

h1 = Height(5, 9)

c1 = h1.cm()

print(h1)
print(c1)

