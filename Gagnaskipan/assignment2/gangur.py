# Choose the one most appropriate of the following ADT for your implementation.
from stack import Stack
from sll import SLList
# Student(s): Jeremias Borjas Tablante, 
#             Sindri Freysson
#             (THE GOATS!!!!)
#                  :-)


def gangur(s: str) -> bool:
    """
    Kattis
    """
    count = 0
    pringles = Stack(SLList())
    for char in s:
        if char == "-":
            continue

        if char == ">":
            pringles.push(char)
            
        if char == "<" and pringles.top():
            count += 1

    return count * len(pringles)

print(gangur(input()))            


        

        
                

         

        
        
        
    



