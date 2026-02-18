a = input()

try:
    a,b,c,d = a.split(".")
    if 0 <= int(a) <= 255:
        last = a

    if 0 <= int(b) <= 255:
        midle_la = b

    if 0 <= int(c) <= 255:
        midle_fi = c

    if 0 <= int(d) <= 255:
        first = d

except:
    print("hello")

print(f"{first}.{midle_fi}.{midle_la}.{last}.in-addr.arpa.")