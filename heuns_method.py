"""
This module uses Heun's Method to solve ordinary differential equations, given an initial condition
"""

from itertools import count, takewhile
from math import sin,cos
from tabulate import tabulate

# the y dash function
ydash = lambda x,y : (sin(x)**3)*y

# initial condition
x = 0
y = 1

h = 0.1  # step


x_start = 0    # the starting x
x_stop = 0.5   # the stopping x (it is not included)

precision = 4   # precision of decimal digits


def print_table(headers:list,data:list):
    print(tabulate(headers=headers,tabular_data=data))


def frange(start, stop, step):
    """ this function used the same the built-in function range() but for FLOAT NUMBERS."""
    return takewhile(lambda x: x< stop, count(start, step))

headers = ['n', 'x', 'xn1', 'k1', 'yn+h*k1', 'k2', 'yn+1',]
max_length_table = []
data = []

k = ydash(x,y)
n = 1
for i in frange(x_start,x_stop,h):
    x = round(i,precision)
    xn1 = round(i+h,precision)
    k1 = round(ydash(x,y),precision)
    yn11 = round(y+k1*h,precision)
    k2 = round(ydash(xn1,yn11),precision)
    ynplus1 = round(y + (h/2)*(k1+k2),precision)

    arr = [n,x,xn1,k1,yn11,k2,ynplus1]
    data.append(arr)

    y = ynplus1
    n += 1

print_table(headers,data)
