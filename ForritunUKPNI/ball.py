# n = int(input())

# not_impostor = []
# impostor = []

# for _ in range((n//2)+1):
#     a,b = map(int, input().split(" "))
#     if a not in not_impostor or b not in not_impostor:
#         not_impostor.append(a)
#         not_impostor.append(b)

#     elif a in not_impostor or b in not_impostor:
#         if a > b:
#             impostor.append(b)
#             impostor.append(a)
#             break
#         else:
#             impostor.append(a)
#             impostor.append(b)
#             break

# print(*impostor)

n = int(input())

pairs = []
impostor = ""

for _ in range((n//2)+1):
    pair: list = input().split()
    if pair[0] in pairs or pair[1] in pairs:
        pair.sort()
        impostor = " ".join(pair)

    pairs += pair

print(impostor)