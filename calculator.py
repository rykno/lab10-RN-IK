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
    if a==0:
        raise ZeroDivisionError
    else:
        return b/a
def logarithm(a,b):
    if a<=0 or a == 1:
        raise ValueError ("base error")
    if b <=0:
        raise ValueError ("error")
    return math.log(b,a)
def exp(a,b):
    return a ** b
def square_root(a):
    if a<0:
        raise ValueError("cant be negative")
    return a ** 0.5
def hypotenuse(a,b):
    return math.hypot(a,b)