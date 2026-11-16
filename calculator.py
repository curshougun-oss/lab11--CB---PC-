"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math
def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def exp(a, b):
    return math.pow(a,b)

def square_root(a):
    if a<0:
        raise ValueError("Cannot calculate square root of negative number")
    else:
        return math.sqrt(a)
    
def hypothenuse(a, b):
    return math.hypot(a, b)

def subtract(a, b):
    return a - b

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Base must be positive and cannot equal 1")
    if b <= 0:
        raise ValueError("Argument must be positive")
    return math.log(b, a)
