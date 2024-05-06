"""
This module uses Heun's Method to solve ordinary differential equations, given an initial condition
"""
from itertools import count, takewhile
from tabulate import tabulate

def print_table(headers:list,data:list):
    """ print table using tabulate function."""
    print(tabulate(headers=headers,tabular_data=data))


def frange(start, stop, step):
    """ this function used the same the built-in function range() but for FLOAT NUMBERS."""
    return takewhile(lambda x: x< stop, count(start, step))
