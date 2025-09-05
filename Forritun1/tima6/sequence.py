count = int(input())

sequence = [1,2,3]

if count <= 3:
    for num in sequence[:count]:
        print(num)


else:
    while len(sequence) < count:
        next_num = sequence[-1] + sequence[-2] + sequence[-3]
        sequence.append(next_num)

    for num in sequence:
        print(num)
