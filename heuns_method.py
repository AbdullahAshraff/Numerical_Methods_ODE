"""
This module uses Heun's Method to solve ordinary differential equations, given an initial condition
"""
from functions_needed import *
from math import sin,cos

# the y dash function
ydash = lambda x,y : (sin(x)**3)*y

# initial condition
x = 0
y = 1

h = 0.1  # step

x_start = 0    # the starting x
x_stop = 0.5   # the stopping x (it is not included)

precision = 5   # precision of decimal digits

headers = ['n', 'x', 'y', 'k1', 'x+h', 'y+h*k1', 'k2', 'yn+1',]
data = []

n = 1
for i in frange(x_start,x_stop,h):
    x = round(i,precision)
    xn1 = round(i+h,precision)
    k1 = round(ydash(x,y),precision)
    yn11 = round(y+k1*h,precision)
    k2 = round(ydash(xn1,yn11),precision)
    ynplus1 = round(y + (h/2)*(k1+k2),precision)

    arr = [n,x,y,k1,xn1,yn11,k2,ynplus1]
    data.append(arr)

    y = ynplus1
    n += 1

print_table(headers,data)
