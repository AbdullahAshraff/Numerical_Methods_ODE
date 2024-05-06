"""
This is the main module
"""
from math import sin
from problem_and_methods import ODEProblem

if __name__ == '__main__':
    ############## user input here #############

    # the y dash function
    ydash = lambda x,y : (sin(x)**3)*y
    initial_point = (0,1) # initial condition


    x_start = 0    # where x starts (inclusive)
    x_stop = 0.5   # where x stops (exclusive)
    h = 0.1  # step

    precision = 5   # precision of decimal digits

    #############################################

    solve_range = {'start': x_start, 'stop': x_stop, 'step': h}
    p = ODEProblem(ydash,initial_point,solve_range,precision)

    print('\n' + '#'*7 + " Euler's Method " + '#'*7)
    p.eulers_method()
    print('\n' + '#'*6 + " Midpoint Method " + '#'*7)
    p.midpoint_method()
    print('\n' + '#'*7 + " Heun's Method " + '#'*8)
    p.heuns_method()
