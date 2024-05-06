"""
This module has ODEProblem class that has the solving numerical methods in it.
"""
from functions_needed import *

class ODEProblem:
    """represents the ode problem that need to be solved by numerical methods"""
    def __init__(self,ydash,initial_point,solve_range,precision=4) -> None:
        self.ydash = ydash
        self.initial_x = initial_point[0]
        self.initial_y = initial_point[1]
        self.step = solve_range['step']
        self.start = solve_range['start']
        self.stop = solve_range['stop']
        self.precision = precision


    def midpoint_method(self):
        """uses the midpoint method to solve the ode problem and prints the table"""
        headers = ['n', 'x', 'y', 'k1', 'xn+h/2', 'yn+h/2*k1', 'k2', 'yn+1',]
        data = []
        x = self.initial_x
        y = self.initial_y
        n = 1
        for i in frange(self.start,self.stop,self.step):
            x = round(i,self.precision)
            xn1 = round(i+self.step/2,self.precision)
            k1 = round(self.ydash(x,y),self.precision)
            yn11 = round(y+k1*self.step/2,self.precision)
            k2 = round(self.ydash(xn1,yn11),self.precision)
            ynplus1 = round(y + self.step*k2,self.precision)

            arr = [n,x,y,k1,xn1,yn11,k2,ynplus1]
            data.append(arr)

            y = ynplus1
            n += 1

        print_table(headers,data)

    def heuns_method(self):
        """uses the heun's method to solve the ode problem and prints the table"""
        headers = ['n', 'x', 'y', 'k1', 'x+h', 'y+h*k1', 'k2', 'yn+1',]
        data = []
        x = self.initial_x
        y = self.initial_y
        n = 1
        for i in frange(self.start,self.stop,self.step):
            x = round(i,self.precision)
            xn1 = round(i+self.step,self.precision)
            k1 = round(self.ydash(x,y),self.precision)
            yn11 = round(y+k1*self.step,self.precision)
            k2 = round(self.ydash(xn1,yn11),self.precision)
            ynplus1 = round(y + (self.step/2)*(k1+k2),self.precision)

            arr = [n,x,y,k1,xn1,yn11,k2,ynplus1]
            data.append(arr)

            y = ynplus1
            n += 1

        print_table(headers,data)

    def eulers_method(self):
        """uses the euler's method to solve the ode problem and prints the table"""
        headers = ['n', 'x', 'y', 'k', 'yn+1',]
        data = []
        x = self.initial_x
        y = self.initial_y
        k = self.ydash(x,y)
        n = 1
        for i in frange(self.start,self.stop,self.step):
            x = round(i,self.precision)
            k = round(self.ydash(x,y),self.precision)
            ynplus1 = round(y+k*self.step,self.precision)

            arr = [n,x,y,k,ynplus1]
            data.append(arr)

            y = ynplus1
            n += 1

        print_table(headers,data)
    def __str__(self):
        return f"the problem is:\ny' = {self.ydash}\n with initial condition ({self.initial_x},{self.initial_y})\n with x range {self.start}:{self.stop} with a step = {self.step}"
