#https://github.com/rykno/lab10-RN-IK.git
#Partner 1:Ryan Nguyen
#Partner 2:Ishaan Krishna

import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    return a + b
def subtract(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        raise ZeroDivisionError
    else:
        return a/b
def logarithm(a,b):
    if a<=0 or a == 1:
        raise ValueError
    if b <=0:
        raise ValueError
    return math.log(b,a)
def exp(a,b):
    return a ** b
def square_root(a):
    if a<0:
        raise ValueError
    return a ** 0.5
def hypotenuse(a,b):
    return math.hypot(a,b)