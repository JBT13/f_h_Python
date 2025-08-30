N= int(input())
M= int(input())
for x in range(N):
    if N % M == 1:
        print("*"*M)
    elif N % M == 0:
        print("*"(M/N))
