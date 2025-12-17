left = "qwertasdfgzxcvb"
right = "yuiophjklnm"

word = input()

a_list = []
b_list = []
for index, value in enumerate(word):
    if index % 2 == 0:
        if value in left:
            a_list.append(1)
        elif value in right:
            a_list.append(110)
    
    if index % 2 != 0:
        if value in right:
            a_list.append(1)
        else:
            a_list.append(110)


for index, value in enumerate(word):
    if index % 2 == 0:
        if value in right:
            b_list.append(1)
        elif value in left:
            b_list.append(110)
    
    if index % 2 != 0:
        if value in left:
            b_list.append(1)
        else:
            b_list.append(110)


if sum(a_list)/len(a_list) == 1 or sum(b_list)/len(b_list) == 1:
    print("yes")

else:
    print("no")



