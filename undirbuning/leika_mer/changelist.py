list = [1,2,3,4]

last = list[-1]
first = list[0]

list[0] = last
list[-1] = first

print(*list)