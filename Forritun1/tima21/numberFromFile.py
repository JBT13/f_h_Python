def everything():
    try:
        file_name = input()
        file = open(f"{file_name}", "r")
        my_list = []
        for line in file.readlines():
            for word in line.split(" "):
                try:
                    word = int(word)
                    my_list.append(word)
                except:
                    continue
        print(sorted(my_list))
    except:
        print(f"{file_name} not found! Please try again.")
        everything()

everything()
# /src/

