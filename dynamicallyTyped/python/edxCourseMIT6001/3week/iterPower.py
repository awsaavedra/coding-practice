
def iterPower(base, exp):
	r = 1	
	while exp > 0:
		r *= base
		exp -= 1
	return r
print iterPower(2,3)
print iterPower(2,4)

