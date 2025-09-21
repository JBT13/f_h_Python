for count in range(2,3466):
    isprime = True
    for i in range(2, int(count**0.5) + 1):
        if count % i == 0:
            isprime = False
            break

    if isprime:
        print(count)