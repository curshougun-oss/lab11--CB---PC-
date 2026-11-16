"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
<<<<<<< HEAD
import math
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    if a <=0:
        raise ValueError
    return math.log(b,a)

def exp(a, b):
    return math.pow(a,b)

=======
# First example
import math

def add(a, b): 
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if a==0:
        raise ZeroDivisionError
    else:
        return b//a
def logarithm(a,b):
    if a<=1 or b<=0:
        raise ValueError
    else:
        return math.log(b,a)
def exponent(a,b):
    return a**b
>>>>>>> b2f2ed63eba631e61f695d03a63bb3dd08ca1784


