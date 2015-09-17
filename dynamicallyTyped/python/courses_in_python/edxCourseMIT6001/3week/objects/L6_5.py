
#Understanding variables and references
aList = range(1, 6)
bList = aList
aList[2] = 'hello'
print "aList == bList"
print aList == bList

print "aList is bList"
print aList is bList #Why? Explain

print "difference between 'is' and '=='"
print """ 
is will return True if two variables point to the same object, 
== if the objects referred to by the variables are equal. """

print "aList: %s" % aList
print "------------------------------------------------ another list situation--"


cList = range(6, 1, -1)
dList = []
for num in cList:
  dList.append(num)
cList == dList #True, why?
cList is dList #False, why?

cList[2] = 20
print cList
print dList #Note, d list didn't change since it is a new independent list, a deep copy
