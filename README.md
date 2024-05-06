ODE Numerical Solver
===============

This is a project to solve Ordinary differential equations using numerical methods:
- Euler's Method
- Midpoint Method
- Heun's Method
---
##			Installation
1. make sure that the following libraries are installed: 
	- tabulate

	You can do this using the following command in your terminal

		pip install tabulate

2. then install this repositry in a new folder using the command

		git clone https://github.com/AbdullahAshraff/Numerical_Methods_ODE
---
##			Usage
1. Open main.py and enter the problem data: 
	- `ydash` : the y dash of the problem
	- `initial_point` : the initial condition. ex. (1,0) where x = 1 and y = 0
	- `h` : the step 
	- `x_start` : from where x starts? (inclusive)
	- `x_stop` : to where x stops? (exclusive)
	- `precision` : the number of decimal digits in numbers
	---	
2. Run the code and look at the tables for the three methods printed in your terminal.

##			Example

for the following problem

> y' =  x<sup>2</sup> - 2y
with initial condition = (0,1)
where x range from 0 to 3 with a step 0.5

The tables printed are:
- Euler's Method table

		  n    x      y      k    yn+1
		---  ---  -----  -----  ------
		  1  0    1      -2      0
		  2  0.5  0       0.25   0.125
		  3  1    0.125   0.75   0.5
		  4  1.5  0.5     1.25   1.125
		  5  2    1.125   1.75   2
		  6  2.5  2       2.25   3.125

- Midpoint Method table

		  n    x        y        k1    xn+h/2    yn+h/2*k1        k2     yn+1
		---  ---  -------  --------  --------  -----------  --------  -------
		  1  0    1        -2            0.25      0.5      -0.9375   0.53125
		  2  0.5  0.53125  -0.8125       0.75      0.32812  -0.09374  0.48438
		  3  1    0.48438   0.03124      1.25      0.49219   0.57812  0.77344
		  4  1.5  0.77344   0.70312      1.75      0.94922   1.16406  1.35547
		  5  2    1.35547   1.28906      2.25      1.67773   1.70704  2.20899
		  6  2.5  2.20899   1.83202      2.75      2.667     2.2285   3.32324

- Heun's Method table

		  n    x        y        k1    x+h    y+h*k1    k2     yn+1
		---  ---  -------  --------  -----  --------  ----  -------
		  1  0    1        -2          0.5     0      0.25  0.5625
		  2  0.5  0.5625   -0.875      1       0.125  0.75  0.53125
		  3  1    0.53125  -0.0625     1.5     0.5    1.25  0.82812
		  4  1.5  0.82812   0.59376    2       1.125  1.75  1.41406
		  5  2    1.41406   1.17188    2.5     2      2.25  2.26953
		  6  2.5  2.26953   1.71094    3       3.125  2.75  3.38476

---
##			Author
This project is made by Abdullah Ashraf.
See copyrights and licensing terms in [LICENSE](/LICENSE)
