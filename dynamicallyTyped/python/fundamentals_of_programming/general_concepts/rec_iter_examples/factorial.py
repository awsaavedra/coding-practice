def factorial(n):
  if n == 0:
    return 1
  else:
    return n*factorial(n-1)


print factorial(6) #6*5*4*3*2*1


def facIter(n):
  sum = 1
  i = n
  while i != 0:
    sum *= i
    i -= 1
  return sum

print facIter(6)
