n = int(input())
full_name_dict = {}
first_name = {}
last_name = {}

for _ in range(n):
    full_name = input()

    full_name_dict[full_name] = True

    if " " in full_name:
        first, last = full_name.split()
        first_name[first] = full_name
        last_name[last] = full_name

    else:
        first_name[full_name] = full_name

m = int(input())
result = []

for _ in range(m):
    name = input()
    if name in full_name_dict:
        result.append("Jebb")
    elif name in first_name:
        result.append(f"Neibb en {first_name[name]} er heima")
    else:
        result.append("Neibb")
for i in result:
    print(i)
