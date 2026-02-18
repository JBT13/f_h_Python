from mat import Mat
from vec import Vec
from math import cos, sin, radians


def is_almost_equal(A, B):
    '''
    Input:
      - A: a matrix or vector
      - B: a matrix or vector with same domain as A
    Output:
      - True if A and B are nearly equal, False otherwise

    The doctests and auto-grader on Gradescope uses this functionality to compare equality to prevent floating-point precision errors.
    '''
    assert A.D == B.D
    s = 0
    C = A - B
    for x in C.f.values():
        y = abs(x)
        s += y*y
    return s < 1e-5


def identity_matrix(D):
    '''
    Input:
      - D: a set representing the row and column domain of the matrix
    Output:
      - A square identity matrix with domain (D, D)
    Examples:
      >>> identity_matrix({0, 1}) == Mat(({0, 1}, {0, 1}), {(0, 0): 1, (1, 1): 1})
      True
      >>> identity_matrix({'x', 'y'}) == Mat(({'x', 'y'}, {'x', 'y'}), {('x', 'x'): 1, ('y', 'y'): 1})
      True
    '''
    dic = {}
    for value in D:
        dic[(value, value)] = 1


    return Mat((D,D), dic)


def are_inverses(A, B):
    '''
    Input:
      - A: a matrix
      - B: a matrix
    Output:
      - True if A and B are inverses, False otherwise
    Examples:
      >>> A = Mat(({0,1}, {0,1}), {(0,0): 1, (1,1): 1})
      >>> B = Mat(({0,1}, {0,1}), {(0,0): 1, (1,1): 1})
      >>> are_inverses(A, B)
      True

      >>> C = Mat(({0,1}, {0,1}), {(0,1): 1, (1,0): 1})
      >>> are_inverses(A, C)
      False
    '''
    assert A.D[0] == B.D[1] and A.D[1] == B.D[0]

    AB = A*B
    BA = B*A

    return identity_matrix(AB.D[0]) == AB and identity_matrix(BA.D[0]) == BA


def rotation_matrix_2d(D, deg):
    '''
    Input:
      - D: a set of two elements representing the row and column domain of the matrix
      - deg: the angle of rotation in degrees
    Output:
      - A 2x2 rotation matrix that rotates vectors by deg degrees
    NOTE:
      - Assume that the smaller element in D appears first in the row and column ordering. Sorting D may be helpful.
    Examples:
      >>> is_almost_equal(rotation_matrix_2d({0,1}, 90), Mat(({0, 1}, {0, 1}), {(0, 0): 0.0, (0, 1): -1.0, (1, 0): 1.0, (1, 1): 0.0}))
      True

      >>> is_almost_equal(rotation_matrix_2d({'x', 'y'}, 180), Mat(({'x', 'y'}, {'x', 'y'}), {('x', 'x'): -1.0, ('x', 'y'): -0.0, ('y', 'x'): 0.0, ('y', 'y'): -1.0}))
      True
    '''

    degres = radians(deg)
    sort = sorted(D)
    x, y = sort
    new_dic = dict()

    new_dic[x,x] = cos(degres)
    new_dic[x,y] = -sin(degres)
    new_dic[y,x] = sin(degres)
    new_dic[y,y] = cos(degres)

    return Mat((D,D), new_dic)



  
  
def rotate_2d(v:Vec, deg):
    '''
    Input:
      - v: a 2D column vector represented as a `Vec` object
      - deg: the angle of rotation in degrees
    Output:
      - A new vector representing v rotated by deg degrees
    Examples:
      >>> v = Vec({0, 1}, {0: 1, 1: 0})  # Vector (1,0)
      >>> is_almost_equal(rotate_2d(v, 90), Vec({0, 1}, {0: 0.0, 1: 1.0}))  # Rotated to (0,1)
      True

    return Vec(v.D, dic)

      >>> v = Vec({0, 1}, {0: 0, 1: 1})  # Vector (0,1)
      >>> is_almost_equal(rotate_2d(v, 90), Vec({0, 1}, {0: -1.0, 1: 0.0}))  # Rotated to (-1,0)
      True
    '''
    assert len(v.D) == 2

    matrix = rotation_matrix_2d(v.D, deg)

    result = matrix * v
  
    return result




if __name__ == "__main__":
    import doctest
    doctest.testmod()
