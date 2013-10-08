from swampy.TurtleWorld import *
import math

world=TurtleWorld()
bob=Turtle()
bob.delay=0.01
def koch(t,length):
	if length<3:
		fd(t,length)
	else:
		koch(t,length/3)
		lt(t,60)
		koch(t,length/3)
		rt(t,120)
		koch(t,length/3)
		lt(t,60)
		koch(t,length/3)

def snowflake(t,length):
	koch(t,length)
	rt(t,120)
	koch(t,length)
	rt(t,120)
	koch(t,length)

snowflake(bob,100)
wait_for_user()
