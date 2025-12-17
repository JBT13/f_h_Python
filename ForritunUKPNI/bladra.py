# a, b = map(int, input().split())

# num_list = []
# for i in range(b):
#     c, d = input().split()
#     num_list.append(int(d))

# if a in num_list:
#     print(min(num_list))

# elif a not in num_list:
#     print(0)


problems, solved = map(int, input().split())

problem_dict = {}

for i in range(1, problems + 1):
    problem_dict[i] = 0

for k in range(solved):
    team, problem = map(int, input().split())
    problem_dict[problem] += 1

minimum_value = problem_dict[1]

for key, value in problem_dict.items():
    if value < minimum_value:
        minimum_value = value

print(minimum_value)