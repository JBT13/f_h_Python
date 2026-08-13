from vec import Vec
from mat import Mat
from matutil import *
from math import sqrt
import svd



def reconstruct_from_svd(U, S, V:Mat):
    '''
    Input:
        - U: a Mat representing the left singular vectors
        - S: a diagonal Mat with singular values
        - V: a Mat representing the right singular vectors

    Output:
        - A Mat representing the reconstructed matrix A
    '''
    v_t = V.transpose
    return U*S*v_t


def frobenius_norm(A):
    '''
    Input:
        - A: a Mat

    Output:
        - A float representing the Frobenius norm of A
    '''
    count = 0
    for value in A.f.values():
        count += value*value

    return sqrt(count)

def rank1_approx(U, S, V):
    '''
    Input:
        - U: a Mat of left singular vectors
        - S: a diagonal Mat of singular values
        - V: a Mat of right singular vectors

    Output:
        - A Mat representing the best rank-1 approximation of the original matrix
    '''
    pass


def frobenius_norm_rank1_approx(U, S, V):
    '''
    Input:
        - U: a Mat of left singular vectors
        - S: a diagonal Mat of singular values
        - V: a Mat of right singular vectors

    Output:
        - A float representing the Frobenius norm of the best rank-1 approximation
    '''
    pass


def solve_least_squares(A, b):
    '''
    Input:
        - A: a Mat representing the matrix in the system Ax ≈ b
        - b: a Vec representing the right-hand side vector

    Output:
        - A Vec representing the least-squares solution x
    '''
    pass



if __name__ == "__main__":
    import doctest
    doctest.testmod()
