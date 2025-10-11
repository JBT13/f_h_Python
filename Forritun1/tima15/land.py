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
        

# You might want to add some functions here, to break the program into smaller steps.


def get_suffix():
    # You can use stderr to display output in command line but not on Gradescope.
    sys.stderr.write(INPUT_PROMPT)
    return input()


# -----------------------------------------------------------------------------------
# You'll often see the following two lines at the bottom of python files.
# This is a good way of setting up the program.
# It checks if this file is being run as the main program.
#
# Python modules have a special attribute called __name__,
# which indicates whether the file is being run as the main program,
# or being imported into another module.
#
# If it is being run, then its __name__ attribute will be "__main__".
# But if it is being imported, it's __name__ will be the name of the .py file.
#
# In case it is being imported, we don't want to run any functions, just import their names.
# But if it is being run, then we call the main() function to start the program.
if __name__ == "__main__":
    main()