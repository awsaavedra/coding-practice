"""
def whileFunc(i):
  numbers = []
  while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
  print "the numbers: " 

  for num in numbers:
    print num
"""
def whileFunc(i):
  numbers = []

  for n in range(i):
    print "At the top n is %d" % n 
    numbers.append(n)

    n = n + 1
    print "Numbers now: ", numbers
    print "At the bottom n is %d" % n 
  print "the numbers: "

  for num in numbers:
    print num

whileFunc(6)

