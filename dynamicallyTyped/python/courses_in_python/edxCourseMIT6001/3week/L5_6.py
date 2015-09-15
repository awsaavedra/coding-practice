#Write an iterative function, lenIter, which computes the length of an input 
#argument (a string), by counting up the number of characters in the string.

def lenIter(aStr):
  aList = list(aStr)
  i = 0
  for x in aList:
    if aList[i] != None:
      i += 1
  return i

print lenIter("abcd")
