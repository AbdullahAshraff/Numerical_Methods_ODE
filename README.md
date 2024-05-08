<p align="center">
	<img src="https://github.com/AbdullahAshraff/Numerical_Methods_ODE/assets/125521810/60559c74-0940-46dd-b1c0-5b9f2e08fe9b">
</p>

ODE Numerical Solver
===============
It's a simple project to solve Ordinary differential equations using numerical methods: Euler's Method, Midpoint Method, and Heun's Method.

#### Contents
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Author](#author)
---
## Installation
1. In a machine with python installed, make sure the following libraries are installed: 
	- tabulate

	You can do this using the following command in your terminal

	```bash
	pip install tabulate
	```
2. then clone this repositry in a new folder using the command

	```bash
	git clone https://github.com/AbdullahAshraff/Numerical_Methods_ODE
	```
---
## Usage
1. Open the file "main.py" and enter the problem data: 
	- `ydash` : the y dash of the problem
	- `initial_point` : the initial condition. ex. (1,0) where x = 1 and y = 0
	- `h` : the step 
	- `x_start` : from where x starts? (inclusive)
	- `x_stop` : to where x stops? (exclusive)
	- `precision` : the number of decimal digits in numbers
2. Run the code and look at the tables for the three methods printed in your terminal.
---
## Example

for the following problem
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;y' =  x<sup>2</sup> - 2y
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;with initial condition = (0,1)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;where x ranges from 0 to 3 with a step 0.5


- #### Data Entered:
	```python
	ydash = lambda x,y : x**2-2*y  # the y dash function

	initial_point = (0,1)  # initial condition

	x_start = 0    # where x starts (inclusive)
	x_stop = 3     # where x stops (exclusive)
	h = 0.5        # step

	precision = 5    # precision of decimal digits
	```
- #### Tables printed:
	- Euler's Method table

			╭─────┬─────┬───────┬───────┬────────╮
			│   n │   x │     y │     k │   yn+1 │
			├─────┼─────┼───────┼───────┼────────┤
			│   1 │ 0   │ 1     │ -2    │  0     │
			│   2 │ 0.5 │ 0     │  0.25 │  0.125 │
			│   3 │ 1   │ 0.125 │  0.75 │  0.5   │
			│   4 │ 1.5 │ 0.5   │  1.25 │  1.125 │
			│   5 │ 2   │ 1.125 │  1.75 │  2     │
			│   6 │ 2.5 │ 2     │  2.25 │  3.125 │
			╰─────┴─────┴───────┴───────┴────────╯

	- Midpoint Method table

			╭─────┬─────┬─────────┬──────────┬──────────┬─────────────┬──────────┬─────────╮
			│   n │   x │       y │       k1 │   xn+h/2 │   yn+h/2*k1 │       k2 │    yn+1 │
			├─────┼─────┼─────────┼──────────┼──────────┼─────────────┼──────────┼─────────┤
			│   1 │ 0   │ 1       │ -2       │     0.25 │     0.5     │ -0.9375  │ 0.53125 │
			│   2 │ 0.5 │ 0.53125 │ -0.8125  │     0.75 │     0.32812 │ -0.09374 │ 0.48438 │
			│   3 │ 1   │ 0.48438 │  0.03124 │     1.25 │     0.49219 │  0.57812 │ 0.77344 │
			│   4 │ 1.5 │ 0.77344 │  0.70312 │     1.75 │     0.94922 │  1.16406 │ 1.35547 │
			│   5 │ 2   │ 1.35547 │  1.28906 │     2.25 │     1.67773 │  1.70704 │ 2.20899 │
			│   6 │ 2.5 │ 2.20899 │  1.83202 │     2.75 │     2.667   │  2.2285  │ 3.32324 │
			╰─────┴─────┴─────────┴──────────┴──────────┴─────────────┴──────────┴─────────╯

	- Heun's Method table

			╭─────┬─────┬─────────┬──────────┬───────┬──────────┬──────┬─────────╮
			│   n │   x │       y │       k1 │   x+h │   y+h*k1 │   k2 │    yn+1 │
			├─────┼─────┼─────────┼──────────┼───────┼──────────┼──────┼─────────┤
			│   1 │ 0   │ 1       │ -2       │   0.5 │    0     │ 0.25 │ 0.5625  │
			│   2 │ 0.5 │ 0.5625  │ -0.875   │   1   │    0.125 │ 0.75 │ 0.53125 │
			│   3 │ 1   │ 0.53125 │ -0.0625  │   1.5 │    0.5   │ 1.25 │ 0.82812 │
			│   4 │ 1.5 │ 0.82812 │  0.59376 │   2   │    1.125 │ 1.75 │ 1.41406 │
			│   5 │ 2   │ 1.41406 │  1.17188 │   2.5 │    2     │ 2.25 │ 2.26953 │
			│   6 │ 2.5 │ 2.26953 │  1.71094 │   3   │    3.125 │ 2.75 │ 3.38476 │
			╰─────┴─────┴─────────┴──────────┴───────┴──────────┴──────┴─────────╯

---
##			Author
This project is made by Abdullah Ashraf.
See copyrights and licensing terms in [LICENSE](/LICENSE)
