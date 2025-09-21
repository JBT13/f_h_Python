n = int(input())

seen_numbers = []
# 1. Create a new list to store the duplicate numbers you find
duplicates = []

row_count = 0
while row_count < n/2 + 1:
    people_input = input().split()
    
    people = []
    for item in people_input:
        people.append(int(item))

    for person in people:
        is_duplicate = False
        for seen_person in seen_numbers:
            if person == seen_person:
                is_duplicate = True
                break
        
        # 2. If a duplicate is found, add it to the duplicates list
        if is_duplicate:
            duplicates.append(person)
        
        seen_numbers.append(person)
    
    row_count = row_count + 1

# 3. After the loop is finished, print all the duplicates
# You can use a loop to print them, separated by a space
for dup in duplicates:
    print(dup, end=' ')
