n = int(input())

all_knights = []
for i in range(n):
    hp, dmg = map(int, input().split())
    all_knights.append({"hp": hp, "dmg": dmg})

winner_index = 0

for next_index in range(1, n):
    champion: int = all_knights[winner_index]
    challenger: int = all_knights[next_index]
    
    while champion['hp'] > 0 and challenger['hp'] > 0:

        challenger['hp'] -= champion['dmg']

        if challenger["hp"] <= 0:
            break

        champion['hp'] -= challenger['dmg']

    if champion['hp'] <= 0:
        winner_index = next_index

print(winner_index + 1)
