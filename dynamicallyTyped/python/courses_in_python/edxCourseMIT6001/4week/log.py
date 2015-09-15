def myLog(x, b):
	assert(x > 0), "x is a pos int"
	assert(b>=2), "b >=2"
	if x < b:
		return 0
	else:
		print("x/b:", x/b)
		return 1 + myLog(x/b, b)			
		
print "result should be 4"
print myLog(16,2) 
print myLog(15,3)
