"""
This module has some simple functions that are needed in the project
"""
from itertools import count, takewhile
from tabulate import tabulate

def print_table(headers:list,data:list):
    """ print table using tabulate function."""
    print(tabulate(headers=headers,tabular_data=data))


def frange(start, stop, step):
    """for FLOAT NUMBERS, it is used the same as the built-in function range().
    Return an object that produces a sequence from start (inclusive) to stop (exclusive) by step."""
    return takewhile(lambda x: x< stop, count(start, step))
