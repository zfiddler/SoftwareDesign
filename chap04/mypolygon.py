from swampy.TurtleWorld import *
import math

world=TurtleWorld()
bob=Turtle()
bob.delay=0.01
def square(t,length):
	for i in range(4):
		fd(t,length)
		lt(t)

def polygon(t,length,n):
	for i in range(n):
		fd(t,length)
		lt(t,360.0/n)


def circle(t,r):
	
	length=2*math.pi*r/100
	polygon(t,length,100)

def arc(t,r,angle):
	length = 2*math.pi*r/360.0
	for i in range(angle):
		fd(t,length)
		lt(t,1)


arc(bob,50,360)


wait_for_user()
