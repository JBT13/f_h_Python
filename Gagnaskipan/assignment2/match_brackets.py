# Choose the one most appropriate of the following ADT for your implementation.
from stack import Stack
import queue
import deque
from sll import SLList
# Student(s): Jeremias Borjas Tablante, 
#             Sindri Freysson
#             (THE GOATS!!!!)
#                  :-)


def match_brackets(s: str) -> bool:
    """
    Returns True if the sting has matching brackets, otherwise False.
    The program checks if for each bracket ( '(', '[' '}' ) there is a matching
    closing bracket. Note, the order and type of the brackets is important.
    For example, if you open a '(' and then a '[', then you need to "close" first
    the ']' before the ')'.
    An example of a matching bracket sting is for example
        "(a [b (c {dd} ) ] [2] )"
    where the following strings are not:
        "(a [b ) ]"  <--- closes [ with a )
        "]b ["   <--- close with ] before opening
        "{{ a }"   <-- missing }
    """
    values = {
        "}":"{",
        ")":"(",
        "]":"["
    }
    ls_values = ["{", "}", "[", "]", "(", ")"]

    pringles = Stack(SLList())
    if s == "":
        return True
    
    for char in s:
        if char not in ls_values:
            continue

        if not values.get(char, False):
            pringles.push(char)
            
        elif not pringles.is_empty() and values[char] == pringles.top():
            pringles.pop()
        
        else:
            return False
    
    return pringles.is_empty()

def main():
    name = 'brackets.txt'
    try:
        with open(name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                print(f'{line:40} {match_brackets(line)}')
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

