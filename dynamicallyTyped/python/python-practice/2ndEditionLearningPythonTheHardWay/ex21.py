#TODO: EXTRA CREDIT PUZZLE
def add(a,b):
  print "ADDING %d + %d " %(a,b)
  return a + b

def subtract(a,b):
  print "SUBTRACTING %d - %d" %(a,b)
  return a-b

def multiply(a,b):
  print "MULTIPLYING %d * %d" %(a,b)
  return a*b

def divide(a,b):
  print "DIVIDING %d / %d " %(a,b)
  return a/b

print "Time for some math with just functions!"

age = add(10,5)
height = subtract(80,4)
weight = multiply(5,20)
iq = divide(274,2)

print "So you are... age: %d, height: %d, weight: %d, iq: %d"%(age,height,weight,iq)

print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq,2))))
#do this for extra credit: create a formula that outputs the same

print "That becomes: ", what, "Can you do it by hand?"