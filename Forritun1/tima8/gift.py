amount = int(input())
list = []

while amount != len(list):
    gift = input()
    parts = gift.split()
    list.append((int(parts[1]),parts[0]))
    
maxi = max(list)    

print(maxi[1])



