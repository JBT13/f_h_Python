from mat import Mat
from vec import Vec
from orthogonalization import orthogonalize


EPS = 1e-10


def norm(v:Vec):
    '''
    Input: A Vec v
    Output: The Euclidean norm (magnitude) of v

    >>> from vec import Vec
    >>> D = {'a', 'b', 'c'}
    >>> v = Vec(D, {'a': 3, 'b': 4, 'c': 0})
    >>> round(norm(v), 6)
    5.0
    '''

    return (v * v)**0.5


def normalize(v:Vec):
    '''
    Input: A Vec v
    Output: A unit vector in the same direction as v, or the zero vector if v is zero

    >>> from vec import Vec
    >>> D = {'a', 'b', 'c'}
    >>> v = Vec(D, {'a': 1, 'b': 2, 'c': 2})
    >>> normalize(v) == Vec(D, {'a': 1/3, 'b': 2/3, 'c': 2/3})
    True
    '''
    length = norm(v)
    if length == 0:
        return Vec(v.D, {})
    
    new = {}
    for key,values in v.f.items():
        new[key] = values/length

    return Vec(v.D, new)

def orthonormalize(L: list[Vec]):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list Lstar of len(L) orthonormal Vecs such that, for all i in range(len(L)),
            Span L[:i+1] == Span Lstar[:i+1]

    >>> from vec import Vec
    >>> D = {'a','b','c','d'}
    >>> L = [Vec(D, {'a':4,'b':3,'c':1,'d':2}), Vec(D, {'a':8,'b':9,'c':-5,'d':-5}), Vec(D, {'a':10,'b':1,'c':-1,'d':5})]
    >>> result = orthonormalize(L)
    >>> expected = [Vec(D, {'a': 0.73, 'b': 0.548, 'c': 0.183, 'd': 0.365}), Vec(D, {'a': 0.187, 'b': 0.403, 'c': -0.566, 'd': -0.695}), Vec(D, {'a': 0.528, 'b': -0.653, 'c': -0.512, 'd': 0.181})]
    >>> all(round(result[i] * expected[i], 3) == 1 for i in range(len(L)))
    True
    '''

    new = []
    for vector in L:
        ortho = vector 

        for u in new:
            ortho = ortho - (u * vector) * u

        if norm(ortho) > EPS:
            new.append(normalize(ortho))

    return new


def inner_product(u: Vec, v: Vec):
    '''
    Input: Two Vecs u and v
    Output: The inner (dot) product of u and v

    >>> from vec import Vec
    >>> D = {'x', 'y'}
    >>> u = Vec(D, {'x': 3, 'y': 4})
    >>> v = Vec(D, {'x': 2, 'y': -1})
    >>> inner_product(u, v)
    2
    '''
    result = 0
    for key in u.f.keys():
        result += u[key] * v[key]

    return result


def projection(u: Vec, v: Vec):
    '''
    Input: Two Vecs u and v
    Output: The projection of u onto v

    >>> from vec import Vec
    >>> D = {'x', 'y'}
    >>> u = Vec(D, {'x': 3, 'y': 4})
    >>> v = Vec(D, {'x': 1, 'y': 0})
    >>> projection(u, v) == Vec(D, {'x': 3.0, 'y': 0.0})
    True
    '''
    dot_v = inner_product(v,v)
    if abs(dot_v) < EPS:
        return Vec(v.D, {})

    pro = inner_product(u,v) / dot_v

    return pro * v


def is_orthogonal(u, v):
    '''
    Input: Two Vecs u and v
    Output: True if u and v are orthogonal (inner product is close to zero), otherwise False

    >>> from vec import Vec
    >>> D = {'x', 'y'}
    >>> u = Vec(D, {'x': 1, 'y': 2})
    >>> v = Vec(D, {'x': -2, 'y': 1})
    >>> is_orthogonal(u, v)
    True
    '''
    
    return inner_product(u,v) == 0


def distance_to_subspace(L, u:Vec):
    '''
    Input: 
        - L: A list of Vecs forming a basis for a subspace
        - u: A Vec to compute the shortest distance to the subspace spanned by L
    Output: The shortest distance from u to the subspace spanned by L

    >>> from vec import Vec
    >>> D = {'x', 'y'}
    >>> L = [Vec(D, {'x': 1, 'y': 0})]
    >>> u = Vec(D, {'x': 3, 'y': 4})
    >>> round(distance_to_subspace(L, u), 6)
    4.0
    '''
    orthol = orthonormalize(L)
    projec = Vec(u.D, {})
    for v1 in orthol:
        projec += (u*v1) * v1

    return norm(u - projec)
     

def is_orthonormal_basis(L):
    '''
    Input: A list L of Vecs
    Output: True if L forms an orthonormal basis (each vector has unit norm and all are mutually orthogonal), otherwise False

    >>> from vec import Vec
    >>> D = {'x', 'y'}
    >>> L = [Vec(D, {'x': 1, 'y': 0}), Vec(D, {'x': 0, 'y': 1})]
    >>> is_orthonormal_basis(L)
    True
    '''
    for i, v1 in enumerate(L):
        if abs(norm(v1) - 1) > EPS:
            return False

        for v2 in L[i+1:]:
            if not is_orthogonal(v1,v2):
                return False

    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()

