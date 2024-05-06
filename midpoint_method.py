"""
This module uses Mid Point Method to solve ordinary differential equations, given an initial condition
"""
from functions_needed import *

def midpoint_method(ydash,x,y,h,x_start,x_stop,precision):
    headers = ['n', 'x', 'y', 'k1', 'xn+h/2', 'yn+h/2*k1', 'k2', 'yn+1',]
    data = []

    k = ydash(x,y)
    n = 1
    for i in frange(x_start,x_stop,h):
        x = round(i,precision)
        xn1 = round(i+h/2,precision)
        k1 = round(ydash(x,y),precision)
        yn11 = round(y+k1*h/2,precision)
        k2 = round(ydash(xn1,yn11),precision)
        ynplus1 = round(y + h*k2,precision)

        arr = [n,x,y,k1,xn1,yn11,k2,ynplus1]
        data.append(arr)

        y = ynplus1
        n += 1

    print_table(headers,data)
