n = int(input())

ls = ["?"]
total = 0

for i in range(1,n+1):
    ls.append(str(i))
    total += i * n

print(" ".join(ls))

m = int(input())

index = m - total

print(f"! {ls[index]}")



# index = 1
# while True:
#     if index != 1:
#         question[index - 1] = 0

#     question[index] = 10
#     print(*question, flush=True)
#     weight = int(input())
#     if weight == (10 * (n + 1 )):
#         question = [f"! {index}"]
#         break
#     index += 1


# print(*question, flush=True)