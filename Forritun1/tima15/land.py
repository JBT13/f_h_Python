import sys

COUNTRIES_OF_THE_WORLD = "/src/countries.txt"
INPUT_PROMPT = "Enter a suffix for a country: "

def main():
    country_suffix = get_suffix()
    file = open(COUNTRIES_OF_THE_WORLD, "r")
    count = 0
    for line in file.readlines():
        line = line.strip()
        if line.endswith(country_suffix):
            print(line)
            count += 1
            
    print(f"{count} countries with suffix {country_suffix} in total.")
        



def get_suffix():
    sys.stderr.write(INPUT_PROMPT)
    return input()



if __name__ == "__main__":
    main()