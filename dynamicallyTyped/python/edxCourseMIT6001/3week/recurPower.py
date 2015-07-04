def recurPower(base, exp):
	if exp == 1:
		return base
	else:
		return base*recurPower(base, exp-1)

print recurPower(2,5)
