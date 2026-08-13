## 1: (Problem 1.7.3) Python Comprehensions: Function Composition
def my_function_composition(f:dict, g:dict):
    '''
    Input:
      -f: a function represented as a dictionary such that g of f exists
      -g: a function represented as a dictionary such that g of f exists
    Output:
      -a dictionary that represents a function g of f
    Examples:
      >>> f = {0:'a',1:'b'}
      >>> g = {'a':'apple','b':'banana'}
      >>> my_function_composition(f,g) == {0:'apple',1:'banana'}
      True

      >>> a = {'x':24,'y':25}
      >>> b = {24:'twentyfour',25:'twentyfive'}
      >>> my_function_composition(a,b) == {'x':'twentyfour','y':'twentyfive'}
      True
    '''
    
    new_dic = {}
    for keys, values in f.items():
        for key2, values2 in g.items():
          if values == key2:
              new_dic[keys] = values2
          
    return new_dic


## 2: Image of a function
def image(f:dict, D:set):
    '''
    Input:
      -f: a function represented as a dictionary
      -D: a set representing the domain of f
    Output:
      -the image of f as a set
    Examples:
      >>> f = {0: 3, 1: 4, 2: 5}
      >>> D = {0, 1}
      >>> image(f, D)
      {3, 4}

      >>> f = {3: 10, 4: 20}
      >>> D = {3, 4}
      >>> image(f, D)
      {10, 20}
    '''

    s = set()
    for value in D:
        if value in f.keys():
            s.add(f[value])

    return s


## 3: Image cardinality of a function
def image_cardinality(f:dict, D:set):
    '''
    Input:
      -f: a function represented as a dictionary
      -D: a set representing the domain of f
    Output:
      -an integer that represents the cardinality of the image of f
    Examples:
      >>> f = {0: 3, 1: 4, 2: 5}
      >>> D = {0, 1}
      >>> image_cardinality(f, D)
      2

      >>> f = {3: 10, 4: 20, 5: 10}
      >>> D = {3, 4, 5}
      >>> image_cardinality(f, D)
      2
    '''
    s = set()
    for value in D:
        if value in f.keys():
            s.add(f[value])

    return len(s)




## 4: One-to-one functions
def is_one_to_one(f:dict, D:set):
    '''
    Input:
      -f: a function represented as a dictionary
      -D: a set representing the domain of f
    Output:
      -a boolean representing whether the function f is one-to-one
    Examples:
      >>> f = {0: 'a', 1: 'b', 2: 'c'}
      >>> D = {0, 1, 2}
      >>> is_one_to_one(f, D)
      True

      >>> f = {0: 'a', 1: 'a', 2: 'b'}
      >>> D = {0, 1, 2}
      >>> is_one_to_one(f, D)
      False
    '''
    s = set()
    for value in D:
        if value in f.keys():
            s.add(f[value])

    return len(s) == len(f)



## 5: Onto functions
def is_onto(f:dict, D:set, C:set):
    '''
    Input:
      -f: a function represented as a dictionary
      -D: a set representing the domain of f
      -C: a set representing the co-domain of f
    Output:
      -a boolean representing whether the function f is onto
    Examples:
      >>> f = {0: 'a', 1: 'b', 2: 'c'}
      >>> D = {0, 1, 2}
      >>> C = {'a', 'b', 'c'}
      >>> is_onto(f, D, C)
      True

      >>> f = {0: 'a', 1: 'b'}
      >>> D = {0, 1}
      >>> C = {'a', 'b', 'c'}
      >>> is_onto(f, D, C)
      False
    '''
    s = set()
    l = set()
    for value in D:
        if value in f.keys():
            s.add(value)

    for value in C:
        if value in f.values():
            l.add(value)

    return s == D and l == C


## 6: Invertible functions
def is_invertible(f:dict, D:set, C:set):
    '''
    Input:
      -f: a function represented as a dictionary
      -D: a set representing the domain of f
      -C: a set representing the co-domain of f
    Output:
      -a boolean representing whether the function f is invertible
    Examples:
      >>> f = {0: 'a', 1: 'b', 2: 'c'}
      >>> D = {0, 1, 2}
      >>> C = {'a', 'b', 'c'}
      >>> is_invertible(f, D, C)
      True

      >>> f = {0: 'a', 1: 'a', 2: 'b'}
      >>> D = {0, 1, 2}
      >>> C = {'a', 'b', 'c'}
      >>> is_invertible(f, D, C)
      False
    '''
    return is_one_to_one(f,D) and is_onto(f,D,C)


## 7: Caesar Cipher Encoder
def encode(s):
    '''
    Input:
      -s: a string consisting only of capitalized letters from the english alphabet
    Output:
      -a string representing the Caesar cipher encoded version of the original string s, shifted by 3 places
    Examples:
      >>> encode("MATRIX")
      'PDWULA'

      >>> encode("XYZ")
      'ABC'
    '''

    new_word = ""
    for letter in s:
        index = (ord(letter) - 65 + 3) % 26
        new = chr(index + 65)
        new_word += new

    return new_word


## 8: Caesar Cipher Decoder
def decode(s):
    '''
    Input:
      -s: a string consisting only of capitalized letters from the english alphabet
    Output:
      -a string representing the Caesar cipher decoded version of the original string s, shifted by 3 places
    Examples:
      >>> decode("PDWULA")
      'MATRIX'

      >>> decode("ABC")
      'XYZ'
    '''
    new_word = ""
    for letter in s:
        index = (ord(letter) - 65 - 3) % 26
        new = chr(index + 65)
        new_word += new

    return new_word

if __name__ == "__main__":
    import doctest
    doctest.testmod()
