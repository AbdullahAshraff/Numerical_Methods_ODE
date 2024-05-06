"""
This module uses Heun's Method to solve ordinary differential equations, given an initial condition
"""
from midpoint_method import *
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

midpoint_method(ydash,x,y,h,x_start,x_stop,precision)
