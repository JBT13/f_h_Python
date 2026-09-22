def precedes(s1:str,s2:str):
    if s1.lower() > s2.lower():
        return s2

    return s1

s1 = input()
s2 = input()

print(precedes(s1,s2))