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

	- #### Example for Euler's Method table
			  n    x        y        k     yn+1
			---  ---  -------  -------  -------
			  0    1        0        1
			  2  0.1  1        0.001    1.0001
			  3  0.2  1.0001   0.00784  1.00088
			  4  0.3  1.00088  0.02583  1.00346
			  5  0.4  1.00346  0.05926  1.00939

	- #### Example for Midpoint Method table

			  n    x        y       k1    xn+h/2    yn+h/2*k1       k2     yn+1
			---  ---  -------  -------  --------  -----------  -------  -------
			  1  0    1        0            0.05      1        0.00012  1.00001
			  2  0.1  1.00001  0.001        0.15      1.00006  0.00334  1.00034
			  3  0.2  1.00034  0.00784      0.25      1.00073  0.01515  1.00185
			  4  0.3  1.00185  0.02586      0.35      1.00314  0.04044  1.00589
			  5  0.4  1.00589  0.0594       0.45      1.00886  0.08302  1.01419

	- #### Example for Heun's Method table

			  n    x        y       k1    x+h    y+h*k1       k2     yn+1
			---  ---  -------  -------  -----  --------  -------  -------
			  1  0    1        0          0.1   1        0.001    1.00005
			  2  0.1  1.00005  0.001      0.2   1.00015  0.00784  1.00049
			  3  0.2  1.00049  0.00785    0.3   1.00128  0.02584  1.00217
			  4  0.3  1.00217  0.02586    0.4   1.00476  0.05934  1.00643
			  5  0.4  1.00643  0.05943    0.5   1.01237  0.11156  1.01498

---
##			Author
This project is made by Abdullah Ashraf.
See copyrights and licensing terms in [LICENSE](/LICENSE)
