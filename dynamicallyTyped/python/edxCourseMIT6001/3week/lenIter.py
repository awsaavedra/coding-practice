'''
Write an iterative function, lenIter, which computes the length of an input 
argument (a string), by counting up the number of characters in the string.
'''
def lenIter(aStr):
	count = 0
	for i in aStr:
		count += 1
	return count

print lenIter("abcd")
print lenIter("")
	
