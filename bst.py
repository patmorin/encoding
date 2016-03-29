#
# This finds the constant in our BST theorem
from __future__ import division

from math import log

def h(p):
    return p*log(1/p,2) + (1-p)*(log(1/(1-p), 2))

def f(c):
    return c*(1-h(1/(c*log(4/3,2))))


lo = 3
hi = 20
for i in range(50):
    m = (lo+hi)/2
    print("{:.30} => {:.30}".format(m, f(m)))    
    if f(m) < 2:
        lo = m
    else:
        hi = m

