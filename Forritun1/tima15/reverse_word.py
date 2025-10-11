def main():
    file_name = input()
    file = open(f"/src/{file_name}")
    for line in file.readlines():
        list = []
        line = line.strip()
        line = line.split()
        for word in line:
            list.append(word[::-1])
        print(*list)

if __name__ == "__main__":
    main()