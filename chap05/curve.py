from swampy.TurtleWorld import *
import math
from math import sqrt

world=TurtleWorld()
bob=Turtle()
bob.delay=0.01

def type_a(t,length,n):
	if n<1:
		return
	if n==1:
		fd(t,length)
		rt(t,60)
		fd(t,length)
		rt(t,120)
		fd(t,length)
		lt(t,60)
		fd(t,length)
		lt(t,120)
		fd(t,length*2)
		lt(t,60)
		fd(t,length)
		rt(t,60)
	else:
		type_a(t,length/sqrt(7), n-1)
		rt(t,60)
		type_b(t,length/sqrt(7), n-1)
		rt(t,120)
		type_b(t,length/sqrt(7), n-1)
		lt(t,60)
		type_a(t,length/sqrt(7), n-1)
		lt(t,120)
		type_a(t,length/sqrt(7), n-1)
		type_a(t,length/sqrt(7), n-1)
		lt(t,60)
		type_b(t,length/sqrt(7), n-1)
		rt(t,60)

def type_b(t,length,n):
	if n<1:
		return
	if n==1:
		lt(t,60)
		fd(t,length)
		rt(t,60)
		fd(t,length*2)
		rt(t,120)
		fd(t,length)
		rt(t,60)
		fd(t,length)
		lt(t,120)
		fd(t,length)
		lt(t,60)
		fd(t,length)
	else:
		lt(t,60)
		type_a(t,length/sqrt(7),n-1)
		rt(t,60)
		type_b(t,length/sqrt(7),n-1)
		type_b(t,length/sqrt(7),n-1)
		rt(t,120)
		type_b(t,length/sqrt(7),n-1)
		rt(t,60)
		type_a(t,length/sqrt(7),n-1)
		lt(t,120)
		type_a(t,length/sqrt(7),n-1)
		lt(t,60)
		type_b(t,length/sqrt(7),n-1)

# for i in range(0,6):
# 	gosper(bob,20,1)

type_a(bob,50,3)

wait_for_user()