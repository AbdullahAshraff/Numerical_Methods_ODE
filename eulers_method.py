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

precision = 4   # precision of decimal digits

headers = ['n', 'x', 'y', 'k', 'yn+1',]
max_length_table = []
data = []

k = ydash(x,y)
n = 1
for i in frange(x_start,x_stop,h):
    x = round(i,precision)
    k = round(ydash(x,y),precision)
    ynplus1 = round(y+k*h,precision)

    arr = [n,x,y,k,ynplus1]
    data.append(arr)

    y = ynplus1
    n += 1

print_table(headers,data)
