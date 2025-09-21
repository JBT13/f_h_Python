# a, b = map(int, input().split())

# cv_set = set()

# for _ in range(a):
#     cv = input()
#     cv_set.add(cv)

# result = []

# for _ in range(b):
#     n = int(input())
#     job_set = set()
#     for _ in range(n):
#         job = input()
#         job_set.add(job)
    

#     if job_set.issubset(cv_set):
#         result.append("apply")

#     else:
#         result.append("why bother?")


# for i in result:
#     print(i)

import sys
input = sys.stdin.readline

a, b = map(int, input().split())

cv_set = set()
for _ in range(a):
    cv_set.add(input().strip())

result = []

for _ in range(b):
    n = int(input())
    job_set = set()
    for _ in range(n):
        job_set.add(input().strip())

    result.append("apply" if job_set.issubset(cv_set) else "why bother?")

print("\n".join(result))
