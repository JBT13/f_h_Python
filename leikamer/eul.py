import numpy as np


# 1. Single Differential Equation Solver
def eul(a, b, y0, n, f):
    t = np.zeros(n + 1)
    w = np.zeros(n + 1)

    t[0] = a
    w[0] = y0
    h = (b - a) / n

    for i in range(n):
        w[i + 1] = w[i] + h * f(t[i], w[i])
        t[i + 1] = t[i] + h

    return t, w


# Example right-hand side function f(t, y)
def f_single(t, y):
    # þetta fall er hægra hlið diffurjöfnunnar
    return y  # Example: dy/dt = y


# 2. System of Differential Equations Solver
def eulhneppi(a, b, y0, n, f):
    y0 = np.array(y0, dtype=float)
    dim = len(y0)

    t = np.zeros(n + 1)
    w = np.zeros((n + 1, dim))

    t[0] = a
    w[0] = y0
    h = (b - a) / n

    for i in range(n):
        w[i + 1] = w[i] + h * np.array(f(t[i], w[i]))
        t[i + 1] = t[i] + h

    return t, w


# Example vector field function f(t, y)
def f_system(t, y):
    # vektorsvið skv. jöfnuhneppinu
    return [y[1], -y[0]]  # Example: Harmonic oscillator


