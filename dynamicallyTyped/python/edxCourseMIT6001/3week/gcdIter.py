'''
The greatest common divisor of two positive integers is the largest integer 
that divides each of them without remainder.
'''

def gcdIter(a, b):
	gcd = min(a,b)
	while gcd > 0:
		if a%gcd == 0 and b%gcd == 0:
			return gcd
		else:
			gcd -= 1
	return gcd	



print gcdIter(2,12)
print gcdIter(6,12)
print gcdIter(9,12)
print gcdIter(17,12)
