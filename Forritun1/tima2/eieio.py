n = int(input())
m = int(input())

for n_kindur in range(0, n+1):
    n_menn = n - n_kindur
    sum_faetur = n_kindur * 4 + n_menn * 2

    if sum_faetur == m:
        print(n_kindur)
        break

else:
    print("Rong talning")
    