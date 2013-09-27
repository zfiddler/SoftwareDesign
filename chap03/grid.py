"""Solution to an exercise in Think Python.

Author: Zoe Fiddler
"""

#draws 1st, 5th and 9th line types
def line1():
	print '+','-','-','-','-', '+','-','-','-','-', '+'

#draws other type of line 
def line2(): 
	print '|',' ',' ',' ' ,' ','|',' ',' ',' ' ,' ','|'

def print_grid():
	line1()
	line2()
	line2()
	line2()
	line2()
	line1()
	line2()
	line2()
	line2()
	line2()
	line1()

print_grid()
