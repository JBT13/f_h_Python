start = int(input("Where to start the range?: "))  # Do not remove this line
end = int(input("Where to stop the range?: "))  # Do not remove this line
increment = int(input("Whats the increment?: "))  # Do not remove this line
# Rewrite the while loop below into a for loop
i = start
for i in range(start,end,increment):
    print(i, end=", ")
    i += increment


