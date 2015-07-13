def FancyDivide(list_of_numbers, index):
    denom = list_of_numbers[index]
    return [SimpleDivide(item, denom)
                for item in list_of_numbers]
                
def SimpleDivide(item, denom):
	try:
		return item / denom
	except ZeroDivisionError, e:
		return 0
print "test below"
print FancyDivide([1,2,3], 0)
print FancyDivide([0, 2, 4], 0)
