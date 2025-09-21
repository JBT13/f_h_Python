# n = int(input())

# list = []
# words = set()
# fair = True

# for i in range(n):
#     things = input()

    
#     if i > 0:
#         last = list[-1][-1]
#         current = things[0]
#         if last != current:
#             if i % 2 == 0:
#                 print("Player 2 lost")
#             else:
#                 print("Player 1 lost")
#             fair = False
#             break

#     if things in words:
#         if i % 2 == 0:
#             print("Player 1 lost")
#         else:
#             print("Player 2 lost")
#         fair = False
#         break

    
#     list.append(things)
#     words.add(things)

# if fair:
#     print("Fair Game")

n = int(input())
words = []
used_words = set()
fair_game = True

for i in range(n):
    word = input()

    if word in used_words:
        if i % 2 == 0:   ## hér er hugsun að í raunu veru það er ekki 2 heldur 3 útaf við byrjum á 0
            print("Player 1 lost")
        else: ##  allt annað sem er ekki odd
            print("Player 2 lost")
        fair_game = False
        break

    # Check Shiritori rule
    if i > 0:
        prev_last = words[-1][-1]
        curr_first = word[0]
        if prev_last != curr_first:
            if i % 2 == 0:
                print("Player 1 lost")
            else:
                print("Player 2 lost")
            fair_game = False
            break

    words.append(word)
    used_words.add(word)

if fair_game:
    print("Fair Game")
