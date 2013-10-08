def is_power(a,b):
	if a==b:
		return True
	elif a%b==0:
		if is_power(a/b,b):
			return True
	else:
		return False


def gcd(a,b):
	if a==0:
		return b
	if b==0:
		return a
	if a>=b:
		r= a%b
		return gcd(b,r)
	if a<b:
		r=b%a
		return gcd(a,r)

print gcd(9,4)
