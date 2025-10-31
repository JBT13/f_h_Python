import io

def main():
    write_list = []
    file_content = open_file()
    if file_content:
        while action(file_content, write_list) != False:
            action(file_content, write_list)

def line_number(number, file:io.TextIOWrapper):
    try:
        number = int(number)
        index = number - 1
        file.seek(0, io.SEEK_SET)
        lines = file.readlines()        
        line = lines[index].strip()
        print(line)

    except :
            print("Invalid line number!")
            return False

def search_str(word, file):
    for line in file:
        line = line.strip()
        if word in line:
            print(line)     


def append_word(word, write_list):
    return write_list.append(word)

def write_file(write_list, content:io.TextIOWrapper):
    content.seek(0, io.SEEK_END)
    for i in write_list:
        content.write(f"\n{i}")


def open_file():
    file_name = input("Enter filename: ")
    try:
        content = open(file_name, "r+")
        return content
    
    except:
        print("File not found")
        return False

def action(file_content:io.TextIOWrapper, write_list):
    action = input("Enter action: ")
    if action == "q":
        file_content.close()
        return False

    elif action[:2] == "l/":
        line_number(action[2:], file_content)
    
    elif action[:2] == "s/":
        search_str(action[2:], file_content)
    
    elif action[:2] == "a/":
        append_word(action[2:], write_list)

    elif action == "w":
        write_file(write_list, file_content)
        



if __name__ == "__main__":
    main()