import math

def bisection(f, a, b, tol):
    '''
    Finds a root of the function f within the interval [a, b] using the bisection method.

    Parameters
    ----------
    f : function
        The function for which to find a root.
    a, b : float
        The starting interval [a, b]. The function values f(a) and f(b) must have opposite signs.
    tol : float
        The desired tolerance. The returned root will be within +/- tol of the actual root.

    Returns
    -------
    float
        An approximation of the root.
    None
        If the method fails (e.g., f(a) and f(b) have the same sign).
        
    Example of use
    --------
    First, define a function. For example, f(x) = x^3 - x - 2.
    >>> def f(x):
    ...     return x**3 - x - 2
    
    Then, call the bisection method with this function.
    >>> bisection(f, 1, 2, 0.005)
    1.521484375
    '''
    # Check if the initial values have opposite signs, which is a necessary condition
    # for the bisection method.
    if f(a) * f(b) >= 0:
        print("Bisection method fails: f(a) and f(b) must have opposite signs.")
        return None

    a_n = a
    b_n = b

    while (b_n - a_n) / 2 > tol:
        m_n = (a_n + b_n) / 2
        f_m_n = f(m_n)

        # If the midpoint is the exact root
        if f_m_n == 0:
            print("Found exact solution.")
            return m_n
        # Check if the root is in the left half of the interval
        elif f(a_n) * f_m_n < 0:
            b_n = m_n
        # If the root is not in the left half, it must be in the right half
        else:
            a_n = m_n
            
    # Return the midpoint of the final interval as the approximation of the root
    return (a_n + b_n) / 2

# Example of how to use the function:

# 1. Define the function you want to find the root of.
#    Let's find the root of f(x) = x^2 - 4, which we know is 2.
def my_function(x):
    return (2000 * math.log(200 / (200 - x)) - 10 * x)-350

# 2. Call the bisection method.
#    We will search for the root in the interval [0, 5] with a tolerance of 0.001.
root = bisection(my_function, 96, 97, 0.00001)

# 3. Print the result.
if root is not None:
    print(f"The approximate root is: {root}")

