# creating non-empty arrays
the_count = [1, 2, 3, 4, 5]
fruits = ["Apples", "Oranges", "Tangerines", "Pears"]
change = [1, "two", 3, "four"]

for number in the_count:
  print "This number %d " % number

for fruit in fruits:
  print "This fruit: %s" % fruit

for i in change:
  print "I got %r" %i

elements = []

for i in range(0,6):
  print "Adding %d to the list." %i
  elements.append(i) #append function:

#Now we can print them out too
for i in elements:
  print "The element was %d" % i