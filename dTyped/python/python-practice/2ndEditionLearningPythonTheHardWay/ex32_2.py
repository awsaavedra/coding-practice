def arrayElementPrint(array):
  for i in range(0,len(array)):
    print array[i]

def arrayIndexPrint(array):
  for i in range(0,len(array)):
    print "Index: %d" %i

def addElementsIntoArray(array):
  for i in range(0,6):
    if i >= 1:
      print "Previous Element: %d" %array[i-1]
    array.append(i)
    print "Added: %d" %array[i]

def removingElementsFromArray(array):
  for i in range(0,len(array)):
    print "removing: %s" % array.pop(0)

print "////////////first module"
arrayElementPrint(["one","two","three","four"])
print "////////////Second module"
arrayIndexPrint(["one","two","three","four"])
print "/////////////Third module"
removingElementsFromArray(["one","two","three","four"])
