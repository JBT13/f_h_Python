f = 0
f1 = 1
n = 10 # Let's find the 10th number (counting from f0=0)

# The correct update is: f, f1 = f1, f + f1

for i in range(n+1):
    # This correctly finds the next number and updates the previous two
    f_old = f1  # Temporarily store the current f1
    f1 = f + f1 # The new f1 is the sum
    f = f_old   # The new f is the old f1

print(f1 - 1) 