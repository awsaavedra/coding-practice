

def whileFunction(arrayIndices):
  incrementBy = 2
  i = 0
  numbers = []
  while i < len(arrayIndices):
    print "At the top i is %d" %i
    numbers.append(i)
    i += incrementBy
    print "Numbers now: ", numbers
    print "At the bottom i is: %d" %i

  print "The numbers: "

  for num in numbers:
    print num

def forFunction(arrayIndices):
  #for i in xrange(start,end, stepSize):
  stepSize = 2
  numbers = []
  for i in xrange(0,len(arrayIndices),stepSize):
    print "At the top i is %d" %i
    numbers.append(i)
    print "Numbers now: ", numbers
    print "At the bottom i is: %d" %i
    pass

#whileFunction([0,1,2,3,4,5,6,7])
forFunction([0,1,2,3,4,5,6,7])