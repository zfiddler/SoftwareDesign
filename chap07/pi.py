import math

def estimate_pi():
	""" estimates pi using srinicasa ramunajan's method

		 no inputs

		 Returns: float
	"""
	total=0.0
	k=0
	while True:
		i=math.factorial(4*k)*(1103.0+26390.0*k)/(math.factorial(k)**4*396**(4*k))
		k=k+1
		total=total+i
		if i<1e-15:
			 break
	total=total*2*math.sqrt(2)/9801.0
	return 1.0/total

x=estimate_pi()
print 'value',
print  x
print 'difference',
print math.pi-x
