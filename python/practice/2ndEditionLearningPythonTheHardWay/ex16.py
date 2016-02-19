#finished Extra credit
from sys import argv

script, filename = argv

print "We are going to erase %r file" %filename
print """If that's alright hit RETURN.
         If that isn't alright, hit CTRL^C(^C)."""
raw_input("?")

print "Opening the file..."
target = open(filename, "w") #why do we need "w" exactly?
target.truncate()

print "Now I am going to ask you for three lines of input..."

line1 = raw_input("Line1: ")
line2 = raw_input("Line2: ")
line3 = raw_input("Line3: ")

#create an array containing each raw input
array = [ line1, line2, line3] #what's right syntax?

for x in xrange(0,3):
  target.write(array[x])
  target.write("\n")
  pass

print "And now we close the file"
target.close()

# If you open the file with ’w’ mode, then do you really need the target.truncate()? Go
# read the docs for Python’s open function and see if that’s true.