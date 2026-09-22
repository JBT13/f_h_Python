import sys
dic = {}

line = input()

while line != "":
    english, fore = line.split()
    dic[fore] = english
    line = input()

for line in sys.stdin:
    word = line.strip()
    print(dic.get(word,"eh"))

