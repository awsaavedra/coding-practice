def twoStr(s1, s2):
	m1 = set(s1)
	m2 = set(s2)
	subStr = "NO"
	if set.intersection(m1,m2):
		subStr = "YES"
	return subStr

if __name__ == "__main__":
	inpt = input()
	for _ in xrange(inpt):
		one = raw_input()
		two = raw_input()
		print twoStr(one, two)



