a,b = map(int, input().split())

author_dc = {}
author_ls = []
for i in range(a):
    n = input()
    book, author = n.split(",")


    if author in author_dc:
        author_dc[author].append(book)
    else:
        author_dc[author] = [book]
        author_ls.append(author)
    
author_ls.sort()

library = []
for auth in author_ls:
    book_list = author_dc[auth]
    book_list.sort()
    library.extend(book_list)


dic = {}
for index,value in enumerate(library):
    dic[value] = index+1

for i in range(b):
    k = input()
    if k in dic:
        print(dic[k]) 
    
    else:
        print(-1)
