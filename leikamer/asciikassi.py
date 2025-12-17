N = int(input())
S = N + 2

if N == 0:
    print("++")
    print("++")

for i in range(S):
    row_str = ""
    for j in range(S):
        if i == 0 or i == S - 1:
            if j == 0 or j == S - 1:
                row_str += "+"
            else:
                row_str += "-"
        else:
            if j == 0 or j == S - 1:
                row_str += "|"
            else:
                row_str += " "
    
    print(row_str)

