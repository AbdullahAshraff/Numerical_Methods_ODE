"""
This is the main module
"""
from ODEProblem import *
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


p = ODEProblem(ydash,x,y,h,x_start,x_stop,precision)

print('\n' + '#'*7 + " Euler's Method " + '#'*7)
p.eulers_method()
print('\n' + '#'*6 + " Midpoint Method " + '#'*7)
p.midpoint_method()
print('\n' + '#'*7 + " Heun's Method " + '#'*8)
p.heuns_method()
