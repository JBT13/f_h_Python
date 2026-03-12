#
# Test program to test the SSL, DDL (partially), and Deque implementations.
# Nice way to do that is to ensure my deque same as Pythons!
#
import random
random.seed(42)  # Fix the seed, such that result is reproducible.

from collections import deque # Python's deque

from dll import DLList # My implementations
from sll import SLList
from deque import Deque

def testing_deque(n, lst):
    d = deque()
    s = Deque(lst)

    for i in range(n):
        if random.random() > 0.5:
            elem = random.randrange(0, 100)
            if random.random() > 0.5:
                d.append(elem)
                s.append(elem)
            else:
                d.appendleft(elem)
                s.appendleft(elem)

        if len(d) == 0:
            continue

        if random.random() > 0.52:
            # elem = random.randrange(0, 100)
            if random.random() > 0.5:
                d.pop()
                s.pop()
            else:
                d.popleft()
                s.popleft()

        if len(d) != len(s):
            print(d, s, len(d), len(s))
            return False

        if not d != s.is_empty():
            print(s)
            return False

        if len(d) > 0:
            if d[0] != s.front():
                return False
            
            if d[-1] != s.back():
                return False

        if str(list(d)) != str(s):
            print(str(list(d)), str(s))
            return False

    return True

if __name__ == '__main__':
    n = 6000
    print(testing_deque(n, SLList()))
    print(testing_deque(n, DLList()))
    # a = [10,20,30]
    # b = a[:]
    # b[2] = 20
    # print(a,b)

