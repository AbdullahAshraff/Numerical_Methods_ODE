"""
This module uses Mid Point Method to solve ordinary differential equations, given an initial condition
"""
from functions_needed import *

class ODEProblem:

    def __init__(self,ydash,x,y,h,x_start,x_stop,precision=4) -> None:
        self.ydash =ydash
        self.x =x
        self.y =y
        self.h =h
        self.x_start =x_start
        self.x_stop =x_stop
        self.precision =precision


    def midpoint_method(self):
        headers = ['n', 'x', 'y', 'k1', 'xn+h/2', 'yn+h/2*k1', 'k2', 'yn+1',]
        data = []
        x = self.x
        y = self.y
        n = 1
        for i in frange(self.x_start,self.x_stop,self.h):
            x = round(i,self.precision)
            xn1 = round(i+self.h/2,self.precision)
            k1 = round(self.ydash(x,y),self.precision)
            yn11 = round(y+k1*self.h/2,self.precision)
            k2 = round(self.ydash(xn1,yn11),self.precision)
            ynplus1 = round(y + self.h*k2,self.precision)

            arr = [n,x,y,k1,xn1,yn11,k2,ynplus1]
            data.append(arr)

            y = ynplus1
            n += 1

        print_table(headers,data)

    def heuns_method(self):
        headers = ['n', 'x', 'y', 'k1', 'x+h', 'y+h*k1', 'k2', 'yn+1',]
        data = []

        x = self.x
        y = self.y
        n = 1
        for i in frange(self.x_start,self.x_stop,self.h):
            x = round(i,self.precision)
            xn1 = round(i+self.h,self.precision)
            k1 = round(self.ydash(x,y),self.precision)
            yn11 = round(y+k1*self.h,self.precision)
            k2 = round(self.ydash(xn1,yn11),self.precision)
            ynplus1 = round(y + (self.h/2)*(k1+k2),self.precision)

            arr = [n,x,y,k1,xn1,yn11,k2,ynplus1]
            data.append(arr)

            y = ynplus1
            n += 1

        print_table(headers,data)
    
    def eulers_method(self):
        headers = ['n', 'x', 'y', 'k', 'yn+1',]
        data = []
        x = self.x
        y = self.y
        k = self.ydash(x,y)
        n = 1
        for i in frange(self.x_start,self.x_stop,self.h):
            x = round(i,self.precision)
            k = round(self.ydash(x,y),self.precision)
            ynplus1 = round(y+k*self.h,self.precision)

            arr = [n,x,y,k,ynplus1]
            data.append(arr)

            y = ynplus1
            n += 1

        print_table(headers,data)
