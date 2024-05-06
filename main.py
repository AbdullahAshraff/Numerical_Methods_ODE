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
print('#'*5 + "Euler's Method" + '#'*5)
p.eulers_method()
print()
print('#'*20)
print('#'*5 + "midpoint Method" + '#'*5)
p.midpoint_method()
print()
print('#'*20)
print('#'*5 + "heun's Method" + '#'*5)
p.heuns_method()
