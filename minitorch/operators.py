"""Collection of the core mathematical operators used throughout the code base."""

import math
import typing

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.

def mul(x: float, y: float):
    return x * y

def id(x: float):
    return x

def add(x: float, y: float):
    return x + y

def neg(x: float):
    return -x

def lt(x: float, y: float):
    return x < y

def eq(x: float, y: float):
    return x == y

def max(x: float, y: float):
    return x if x >= y else y

def is_close(x: float, y: float):
    return math.isclose(x, y)

def sigmoid(x: float):
    return 1 / (1 + math.e ** neg(x))

def relu(x: float):
    return max(0, x)

def log(x: float):
    return math.log(x)

def exp(ex: float):
    return math.e ** ex

def inv(x: float):
    return 1 / x

'''
d/dx(ln(x)) = 1/x
'''
def log_back(x: float, y: float):
    return y / x 

def inv_back(x: float, y: float):
    return neg(1 / (x**2)) * y

def relu_back(x: float, y: float):
    return (1.0 if x > 0 else 0.0) *  y

# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.

def map(it: Iterable, la: Callable):
    return [la(x) for x in it]

def zipWith(it1: Iterable, it2: Iterable, la: Callable[[typing.Any, typing.Any], typing.Any]):
    return [la(x1, x2) for x1, x2 in zip(it1, it2)]

def reduce(la: Callable, ite: Iterable, init: object = None):
    it = iter(ite)
    if init is None:
        value = next(it)
    else:
        value = init
    for e in it:
        value = la(e, value)
    return value

def negList(l: list[float]):
    return map(l, neg)

def addLists(l1: list[float], l2: list[float]):
    return zipWith(l1, l2, add)

def sum(l: list[float], init: float = 0.0):
    return reduce(sum, l, init)

def prod(l: list[float]):
    return reduce(mul, l, 1)

