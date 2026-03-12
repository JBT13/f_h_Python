import tokenizer
from tokenizer import Tokenizer

# throw/raise this exception if a
# division by zero occurs.
class DivisionByZero(Exception):
    pass

# IMPLEMENT HERE!!!! -----------------------------------------------------
# This function is the actual recursive
# implementation of the prefix parser.
# The tokenizer is pass-by-object-reference
# so it will be the same instance of Tokenizer
# throughout the recursive run.
def prefix_parser_recursive(tokenizer: Tokenizer):
    token = tokenizer.get_next_token()

    if token == "":
        return token

    if token == "+":
        return float(prefix_parser_recursive(tokenizer))+ float(prefix_parser_recursive(tokenizer))
    
    if token == "-":
        return float(prefix_parser_recursive(tokenizer))- float(prefix_parser_recursive(tokenizer))

    if token == "*":
        return float(prefix_parser_recursive(tokenizer))* float(prefix_parser_recursive(tokenizer))
    
    if token == "/":
        x = float(prefix_parser_recursive(tokenizer))
        y = float(prefix_parser_recursive(tokenizer))
        if y == 0:
            raise DivisionByZero
        
        return x/y

    return token
# This function makes the tokenizer
# and then calls the recursive function.
# It is often necessary to make a separate
# recursive function that takes and returns
# particular values that don't match the
# proper functions parameters and return value.
def prefix_parser(str_statement):
    tokenizer = Tokenizer(str_statement)
    return prefix_parser_recursive(tokenizer)

# This is a tester function to test that
# the output and/or error message from the
# prefix_parser function are correct.
def test_prefix_parser(str_statement):
    str_print = str_statement.rstrip()
    try:
        str_print += " = " + str(prefix_parser(str_statement))
    except DivisionByZero:
        str_print += ": " + str("A division by zero occurred")
    print(str_print)

# A few hard coded tests
test_prefix_parser("+ 3 20")
test_prefix_parser("+ / 3 - 21 20 * 2 40")
test_prefix_parser("+ / 3 - 20 20 * 2 40")

# This must be a relative path from the folder that you have open
# in Visual Studio Code.  This particular path works if you open
# the folder PrefixParserBase directly
f = open("prefix_statements.txt", "r")
for line in f:
    test_prefix_parser(line)
f.close()
