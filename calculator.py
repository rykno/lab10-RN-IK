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
def multiply(a,b):
    return a*b
def divide(a,b):
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
def exponent(a,b):
    return a ** b
